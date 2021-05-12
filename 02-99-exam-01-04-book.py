## 자동 로또 번호 생성기 : 책 답안 ver  ##

import random

## 전역 변수 선언 부분
''' 프로그램 구현에 꼭 필요한 작업인가? 가독성을 위한 건가? '''
totalLotto = []
lotto = []  # 함수의 지역변수가 아니라, 포문에 쓰일 변수니까 전역 변수로 미리 선언해야 하는 건가? 대입 연산자 뒤엔 '''를 주석으로 못 씀
pickNum = 0  # 파이썬 문법상으론 필요 없는데, 자바 같은 언어의 경우 미리 선언해두는 게 편하겠지.
count = 0

## 메인 코드 부분
print("** 로또 번호 생성을 시작합니다. **")
count = int(input("몇 줄을 구매하시나요? --> "))

for _ in range(count):  # 언더바로 해도 되다니?? 여기서도 '''이 안 되네? 이걸로 하니까, 아래 줄이 예상치 못한 들여쓰기라고 나옴.
    lotto = []  # lotto 리스트 초기화 문장을 책에서는 for문 맨 첫 명령으로 넣었지만, 난 흐름을 명확히 하기 위해 맨 뒤에.
    while True:
        ''' 무한루프를 돌리고, lotto 길이가 6이 된 순간 break를 하는 게,
            실제로 원하는 기능을 더 직관적으로 구현한 건가? 나의 코드 리뷰는 지금 단계엔 무의미한가? '''
        pickNum = random.randint(1, 45)
        if pickNum not in lotto:
            lotto.append(pickNum)
        if len(lotto) >= 6:  # 두 if 는 동일한 수준으로, 상하관계 아니다.
           break
    totalLotto.append(lotto)  # 무한 루프가 종료된 후에 totalLotto에 넣어야 한다. 실수 주의.

for lotto in totalLotto:  # totalLotto 에서 lotto를 한 줄씩 빼는 작업에 적합한 네이밍이다.
    lotto.sort()  # 책에서는 여기서 sort 하네. 나중에 어떤 기능이 추가 될지 모르니, 담을 때부터 잘 정렬해서 넣는 게 좋을 것 같은데.
    print('자동번호--> ', end='')  # end 기본 값은 개행이기 때문에, 꼭 ''로 지정해줘야 다음 print에서 lotto[0]이 이어져 나온다.
    for i in range(0, 6):
        print("%3d" % lotto[i], end='')  # 역시나, lotto[i]가 한 줄에 이어져 나온다.
    print()  # 하위 for문이 끝나면, 다른 lotto 줄을 엔터 후에 출력하기 위해 print한다. ''를 안 써도 줄이 나온다!
