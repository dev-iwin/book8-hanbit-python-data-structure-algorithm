class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5


print("========04-01 단순 출력========")
print(node1.data, end=' ')
print(node1.link.data, end=' ')
print(node1.link.link.data, end=' ')
print(node1.link.link.link.data, end=' ')
print(node1.link.link.link.link.data, end=' ')


## 04-03 적은 데이터의 단순연결리스트에 새 노드 직접 삽입하기
newNode = Node()
newNode.data = "재남"
newNode.link = node2.link
node2.link = newNode


print("\n========04-02 자동 출력========")
current = node1
print(current.data, end=' ')
while current.link != None:
    current = current.link
    print(current.data, end=' ')


## 04-04 적은 데이터의 단순연결리스트에 중간 노드 직접 삭제하기
node2.link = newNode.link
del(newNode)


print("\n========04-02 재남 삭제 출력========")
current = node1
print(current.data, end=' ')
while current.link != None:
    current = current.link
    print(current.data, end=' ')