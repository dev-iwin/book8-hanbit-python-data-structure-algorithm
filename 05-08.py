## 원형 연결 리스트 활용 : 짝수 홀수 구분 프로그램
import random

## 클래스와 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()

def countOddEven():
    global memory, head, current, pre

    odd, even = 0, 0
    if head == None:
        return False

    current = head
    while True:
        if current.data % 2 == 1:
            odd += 1
        else:
            even += 1
        if current.link == head:
            break
        current = current.link

    return odd, even
    # 이렇게 리턴값이 있도록 함수를 만들고, 함수를 또 다른 함수의 인수로 넣으면. 자동으로 연산되겠구나

def makeNegativeNumber(odd, even):
    if odd > even :
        reminder = 1
    else:
        reminder = 0

    current = head
    while True:
        if current.data % 2 == reminder:
            current.data *= -1
        if current.link == head:
            break
        current = current.link

## 전역 변수
memory = []
head, current, pre = None, None, None

## 메인 코드
if __name__ == "__main__":

    dataArray = []
    for i in range(7):
        dataArray.append(random.randint(1, 100))

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)

    oddCount, evenCount = countOddEven()
    print('홀수: ', oddCount, '\t', '짝수: ', evenCount)

    makeNegativeNumber(oddCount, evenCount)
    printNodes(head)