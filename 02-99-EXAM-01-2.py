##  자동 로또 번호 생성기 ver2 ##
##  동일한 줄을 제거하는 버전 ##

import random

allLotto = []
oneLotto = []
count = 0
numLotto = 0


print("** 로또 번호 생성을 시작합니다. **")
count = int(input("로또를 몇 줄 구매할까요? --> "))

while len(allLotto) <= count:
    while len(oneLotto) <= 6:
        numLotto = random.randint(1, 45)
        if numLotto not in oneLotto:
            oneLotto.append(numLotto)

    oneLotto.sort()
    if oneLotto not in allLotto :
        allLotto.append(oneLotto)
    oneLotto = []

for i in range(len(allLotto)):
    lottoStr = "자동번호-->"
    print(lottoStr, end=' ')
    for k in range(6):
        print("%3d" % allLotto[i][k], end=' ')
    print('')
