## 사용자가 입력한 정보 관리하기
'''
사용자가 이름과 이메일을 입력하면, 이메일 순서대로 단순 연결 리스트를 생성하는 프로그램
'''

## 클래스와 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start

    if current == None:  # 여기에 current.link == None 이라고 실수함
        return

    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def makeSinglyLinkedList(nameEmail):
    global head, current, pre

    if head == None:
        node = Node()
        node.data = nameEmail
        head = node
        memory.append(node)
        return

    current = head
    if current.data[1] > nameEmail[1]:
        node = Node()
        node.data = nameEmail
        node.link = head
        head = node
        memory.append(node)
        return

    while current.link != None:
        pre = current
        current = current.link
        if current.data[1] > nameEmail[1]:
            node = Node()
            node.data = nameEmail
            node.link = current
            pre.link = node
            memory.append(node)
            return

    node = Node()
    node.data = nameEmail
    current.link = node
    memory.append(node)

## 전역 변수
memory =[]
head, current, pre = None, None, None

## 메인 코드
if __name__ == "__main__":

    while True:
        name = input("이름 --> ")
        email = input("이메일 --> ")
        data = [name, email]

        makeSinglyLinkedList(data)
        printNodes(head)