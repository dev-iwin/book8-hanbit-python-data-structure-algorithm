##  자동 로또 번호 생성기  ##

import random


## 전역 변수 선언부
allLotto = []
oneLotto = []
count = 0
numLotto = 0


## 메인 코드부

print("** 로또 번호 생성을 시작합니다. **")
count = int(input("로또를 몇 줄 구매할까요? --> "))

for i in range(count):

    while len(oneLotto) <= 6:
        numLotto = random.randint(1, 45)
        if numLotto not in oneLotto:
            oneLotto.append(numLotto)

    oneLotto.sort()
    allLotto.append(oneLotto)
    oneLotto = []

for i in range(len(allLotto)):
    lottoStr = "자동번호-->"
    print(lottoStr, end=' ')
    for k in range(6):
        print("%3d" % allLotto[i][k], end=' ')
    print('')
