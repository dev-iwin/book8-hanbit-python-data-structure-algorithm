## 이중 연결 리스트 구현
## 클래스 함수
class Node2():
    def __init__(self):
        self.plink = None
        self.data = None
        self.nlink = None

def printNodes(start):
    current = start

    if head == None:
        return

    print('정방향 -->', end=' ')
    print(current.data, end=' ')
    while current.nlink != None:
        current = current.nlink
        print(current.data, end=' ')
    print()

    print('역방향 -->', end=' ')
    print(current.data, end=' ')
    while current.plink != None:
        current = current.plink
        print(current.data, end=' ')
    print()


## 전역 변수
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드
if __name__ == '__main__':

    node = Node2()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node2()
        node.data = data
        pre.nlink = node
        node.plink = pre
        memory.append(node)

    # print(node.data)
    # print(node.plink.data)
    # print(node.nlink.data)

    printNodes(head)
