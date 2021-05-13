## 클래스와 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNode(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def makeSinglyLinkedList(namePhoneHeight):
    global memory, head, current, pre
    printNode(head)

    node = Node()
    node.data = namePhoneHeight
    memory.append(node)
    if head == None:
        head = node
        return

    if head.data[2] > namePhoneHeight[2]:
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[2] > namePhoneHeight[2]:
            pre.link = node
            node.link = current
            return

    current.link = node

## 전역 변수
memory = []
head, current, pre = None, None, None
dataArray = [["지민", "010-1111-1111", 180], ["정국", "010-2222-2222", 177], ["뷔", "010-3333-3333", 183],
             ["슈가", "010-4444-4444", 175], ["진", "010-5555-5555", 179]]

## 메인 코드
if __name__ == "__main__":

    for data in dataArray:
        makeSinglyLinkedList(data)

    printNode(head)
    # 단순연결리스트와 비교를 위한 메모리 출력
    for i in range(len(memory)):
        print(memory[i].data, end=' ')  # 메모리에서는 정말 무작위 순서로 저장되지만, 단순연결리스트의 링크로 순서대로 연결되는구나.