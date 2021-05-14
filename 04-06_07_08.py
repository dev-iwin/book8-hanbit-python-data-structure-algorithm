## 클래스와 함수 선언
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

def insertNode(findData, insertData):
    global memory, head, current, pre

    if head.data == findData :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node
                        # 함수 맨 뒤에 리턴을 굳이 안 넣네? return은 반환값이 아니라 함수 종료를 위한 기능이 기본인가?
def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        print("# 첫 노드가 삭제됨 #")
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            print("# 중간 노드가 삭제됨 #")
            return
    print("# 삭제된 노드가 없음 #")

def findNode(findData):  # 왜 노드 전체를 반환하게 할까? : 항상 출력을 원하는 것이 아니고, 노드를 추출하는 기능만 필요할 수 있으니까! 그래서 빈 노드도 나름 의미가 되나보다.
    global memory, head, current, pre

    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
              return current
    return Node()

## 04-05_06_07 전역 변수 선언
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드
if __name__ == '__main__':
    ## 04-05 데이터 저장소에서 데이터를 가져워서 단순연결리스트 생성
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(head)

    for data in dataArray[1:]:
        pre = node      # 처음에는 pre에 첫 번째 노드가 들어가게 된다.
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
    print("04-05 최초 생성")
    printNodes(head)
    print("04-06 단순연결리스트에 노드 삽입(맨앞, 중간, 마지막)")
    insertNode("다현", "화사")
    printNodes(head)

    insertNode("사나", "솔라")
    printNodes(head)

    insertNode("없음", "문별")
    printNodes(head)
    print("04-07 단순연결리스트에 노드 삭제(맨앞, 그외)")
    deleteNode("다현")
    printNodes(head)

    deleteNode("쯔위")
    printNodes(head)

    deleteNode("지효")
    printNodes(head)

    deleteNode("재남")
    printNodes(head)
    print("04-08 단순연결리스트에 노드 검색")
    fNode = findNode("화사")
    print(fNode.data)

    fNode = findNode("솔라")
    print(fNode.data)

    fNode = findNode("문별")
    print(fNode.data)

    fNode = findNode("재남")
    print(fNode.data)