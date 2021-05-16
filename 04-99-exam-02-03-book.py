## 로또 추첨하기 : 뽑은 숫자를 '크기' 순서대로 정렬하기
import random

## 클래스와 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def makeLottoList(num):
    global memory, head, current, pre

    node = Node()
    node.data = num
    memory.append(node)

    if head == None:
        head = node
        return

    if head.data > num:
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data > num:
            pre.link = node
            node.link = current
            return

    current.link = node

def findNumber(num):
    global memory, head, current, pre

    # findData = num    # 한 번만 쓸거라, 변수를 생성할 필요가 없었네.

    if head == None:    # 단순연결리스트가 비어있으면- 이라는 뜻
       return False     # 근데 이런 의미를 살리려면 "단순 연결 리스트에 데이터 개수가 0이니?"이런 식으로 점검하는 논리 구조를 만들어야 하는 거 아닌가?
                        # 이걸 글로벌 전역변수 head를 가져와서 "이 포인터가 존재해?"라고 묻는 건 너무 우회적이고 간접적인 거 아닌가?? 아닌가 효율적인가?
    current = head
    if current.data == num:     # 굳이 이렇게 같은 if문을 while문 밖에 안에 쓰게 된단 말이지...?? 그러나 오류의 위험은 없는 단순한 코드. 심플이즈베스트
        return True
    while current.link != None:
        current = current.link
        if current.data == num:
            return True
    return False

'''
    current = head
    for i in range(len(memory)): # 사실 여기서만 메모리 길이 = 단순연결리스트 길이 이긴 하니.... 그래서 단순연결리스트를 이름짓는 게 필요하다는 생각인거지만.
        if current.data == num:  # findData:
            return True
        current = current.link  # 단순연결리스트의 데이터가 1개만 있을 때, 불필요하거나 에러를 만들어낼 코드라든가??
                                #  : 이론상 current = None 이 되는 명령이 생김. 복잡한 프로그램에서는 예기치 못한 오류를 야기할지도 모름.
                                # 이렇게 하면, 똑같은 if문 while 밖에 안에 각각 쓸 필요가 없는 것 같기도 하고?? 아닌가???
'''



## 전역 변수
memory = []
head, current, pre = None, None, None


## 메인 코드
if __name__ == "__main__":

    # 뽑은 숫자를 점검하지, 이미 단순연결에 있는 걸 확인하네?
    lottoCount = 0
    while True:
        lotto = random.randint(1, 45)
        if findNumber(lotto):
            continue    # 이미 있으면 추가하지 않기 위해
        makeLottoList(lotto)
        lottoCount += 1
        if lottoCount == 6:  # 왜 책에서는 굳이 >= 6 이라고 했을까?
            break

    printNodes(head)
