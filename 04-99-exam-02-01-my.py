## 로또 추첨하기 : 뽑은 숫자 순서대로 단순연결 리스트로 저장하기
import random

## 클래스와 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    # 근데, head를 인수로 전달할 게 아니라, 단순연결리스트 이름을 넣으면, head부터 훑게 만들어야 하지 않을까?
    # 출력할 때 memory를 출력해야 하는지, head를 넣으면 되는지 헷갈려서 순간 한 번 더 생각하게 만드는 비효율이 나오는데?
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


## 전역 변수
memory = []
head, current, pre = None, None, None


## 메인 코드
if __name__ == "__main__":

    number = int(input("번호를 몇 개 뽑을까요? --> "))
    makeLottoList(number)
    printNodes(head)