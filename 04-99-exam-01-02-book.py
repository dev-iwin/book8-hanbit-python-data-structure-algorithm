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

    if current == None:
        return

    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def makeSinglyLinkedList(nameEmail):
    global head, current, pre

    # 상황별 코드마다 노드 생성 명령 작성할 필요 없음
    node = Node()
    node.data = nameEmail
    memory.append(node)
    if head == None:
        head = node
        return

#   current = head      # 아래줄을 head라고 명시적으로 쓰면 여기에 나올 필요 없음. : 남이 보기 좋은 코드가 better
#   if current.data[1] > nameEmail[1]:
    if head.data[1] > nameEmail[1]:     # 의미(첫 노드와의 비교)도 직관적
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None:
        pre = current           # 위에 주석처리 한 것처럼 하면, if문 전에 이 작업 안 해도 되지 않을까? -- 아닌듯
        current = current.link
        if current.data[1] > nameEmail[1]:
            node.link = current
            pre.link = node     # 책에서는 얘가 윗줄로 가네. 별 상관 없음
            return

    current.link = node


## 전역 변수
memory =[]
head, current, pre = None, None, None

## 메인 코드
if __name__ == "__main__":

    while True:
        name = input("이름 --> ")
        if name == "" or name == None:
            break   # 이름에서 엔터 누르면 종료되게 했음
        email = input("이메일 --> ")
        makeSinglyLinkedList([name, email])  # 이렇게 바로 넣어도 되는군
        printNodes(head)