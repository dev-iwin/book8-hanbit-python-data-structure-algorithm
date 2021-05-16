## 현재 위치부터 가까운 편의점 관리하기
'''
현재 위치를 (0, 0)이라 가정하고, 편의점 위치(x, y)와 거리가 가까운 순서대로 원형 연결 리스트를 생성하는 프로그램
    편의점 10개를 A, B, C, ... 순서로 이름을 부여한다 (대문자 아스키코드 : 65~90)
    편의점 위치 x와 y는 1부터 100까지 랜덤하게 좌표가 생성되도록 한다.
    현재 위치와 편의점 거리는 (x^2 + y^2)의 제곱근(sqrt)으로 계산한다.
    편의점 데이터 1개는 (편의점 이름, x좌표, y좌표) 형식의 튜플로 구성한다.
'''
import random, math

## 클래스와 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printStores(start):
    current = start
    if current == None:
        return

    x, y = current.data[1:]
    print(current.data[0], '편의점, 거리:', math.sqrt(x * x + y * y))
    while current.link != head:  # 이렇게 앞에 없으면, head는 무시되서 10개 편의점 중 9개만 출력됨. 오타임.
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], '편의점, 거리:', math.sqrt(x*x + y*y))

def makeStoreList(storeData):
    global memory, head, current, pre

    node = Node()
    node.data = storeData
    memory.append(node)

    if head == None:
        head = node
        node.link = head
        return

    nodeX, nodeY = node.data[1:]    # 내 버전에서는 storeData[1:]라고 했네. 이게 더 맞는데.
    nodeDist = math.sqrt(nodeX*nodeX + nodeY*nodeY)
    headX, headY = head.data[1:]
    headDist = math.sqrt(headX*headX + headY*headY)

    if headDist > nodeDist:
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        currX, currY = current.data[1:]
        currDist = math.sqrt(currX**2 + currY**2)
        if currDist > nodeDist:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head

## 전역 변수
memory = []
head, current, pre = None, None, None

## 메인 코드
if __name__ == "__main__":

    storeArray = []
    storeName = 'A'
    for i in range(10):
        store = (storeName, random.randint(1, 100), random.randint(1, 100))
        storeArray.append(store)
        storeName = chr(ord(storeName)+1)

    for store in storeArray:
        makeStoreList(store)

    printStores(head)