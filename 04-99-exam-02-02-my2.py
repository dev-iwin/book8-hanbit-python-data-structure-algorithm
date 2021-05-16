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
            node.link = current
            pre.link = node
            return

    current.link = node



'''
def makeLottoList(num):
    global memory, head, current, pre

    lotto = []
    while len(lotto) < num:
        pickNum = random.randint(1, 45)
        if pickNum not in lotto:
            lotto.append(pickNum)

    node = Node()
    node.data = lotto[0]
    memory.append(node)
    head = node
    current = head
    for luckyNum in lotto[1:]:
        node = Node()
        node.data = luckyNum
        current.link = node
        current = node
        memory.append(current)
'''

## 전역 변수
memory = []
head, current, pre = None, None, None


## 메인 코드
if __name__ == "__main__":

    # for i in range(6):
    #     makeLottoList(random.randint(1, 45))
    # printNodes(head)


    lotto = []
    while len(lotto) < 6:
        pickNum = random.randint(1, 45)
        if pickNum not in lotto:
            lotto.append(pickNum)

    for luckyNum in lotto:
        makeLottoList(luckyNum)

    printNodes(head)