## 클래스와 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current.link == None:
        return                      # 데이터 개수가 1개인 단순연결리스트는 일반 print 함수를 쓰면 되니까 그냥 종료되게 만든 건가?
    print(current.data, end=' ')
    while current.link != start :
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre  # 전역변수를 직접 가져다 써야 하는 이유가 있나? 위험하다던데. 함수마다 글로벌 예약어 쓰기도 번거롭고.

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        last = head                 # 원형으로 만들기 위해 추가된 코드 4줄
        while last.link != head:
            last = last.link
        last.link = node            # 마지막 노드의 링크를 맨 앞에 온 새 노드로 설정하기 위해 while 문을 돌린 것
        head = node                 # 그 후에 새 노드를 head 라고 지정해주는 거지!
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()               # 새 노드를 생성하는 코드를 3번이나 써야했는데, 이거 못 줄이나?
    node.data = insertData
    current.link = node
    node.link = head

def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:
        current = head          # 이게 바로 생각이 안 났네. 최종적으로 지우기 작업의 대상을 가리킬 포인터가 필요했단 말이지.
        head = head.link
        last = head
        while last.link != current:  # 추론 가능한 부분이긴 하지만, 나중에 빠르게 기억이 안 날 것 같은 부분이다.
            last = last.link
        last.link = head
        del(current)
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def findNode(findData):
    global memory, head, current, pre

    current = head  # 아 이거부터 시작하는구나
    if current.data == findData:
        print("# 첫 노드에서 찾음 #")
        return current

    while current.link != head:
        # pre = current     # 이거 필요 없었네?
        current = current.link
        if current.data == findData:
            print("# 중간 노드에서 찾음 #")
            return current
    print("# 찾는 노드가 없음 #")          # self study : 반환값으로 같이 출력되게 할 수는 없을까?
    return Node()   # None 아니고 빈 노드로 반환하네? 노드 추출을 원할 때, 없는 노드임을 알려주면서 노드를 추출하고 싶어서? 이후에 빈 노드인 경우 자동 삽입되는 기능이랑 연계될지도 모르는 것!

## 전역 변수
memory = []
head, current, pre = None, None, None
dataArray = ["다현","정연","쯔위","사나","지효"]

## 메인 코드
if __name__ == "__main__":

    print("\n## 05-04 원형 연결 리스트 생성 함수 : 이 예제에서는 어차피 한 번만 이뤄질 동작이라 함수 선언을 안 한 건가?")
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node     # 여기서 살짝 헷갈릴 뻔
        node.link = head
        memory.append(node)

    printNodes(head)

    print("\n## 05-05 원형연결리스트의 노드 삽입")
    insertNode("다현", "화사")
    printNodes(head)

    insertNode("사나", "솔라")
    printNodes(head)

    insertNode("재남", "문별")
    printNodes(head)

    print("\n## 05-06 원형연결리스트의 노드 삭제")
    deleteNode("화사")
    printNodes(head)

    deleteNode("솔라")
    printNodes(head)

    deleteNode("문별")
    printNodes(head)

    deleteNode("재남")
    printNodes(head)

    print("\n## 05-07 원형연결리스트의 노드 검색")
    fNode = findNode("다현")
    print(fNode.data)

    fNode = findNode("쯔위")
    print(fNode.data)

    fNode = findNode("재남")
    print(fNode.data)