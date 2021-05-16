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

def printStoreOrder(start):
    current = start
    if current == None:
        return
    print(current.data[0], '편의점, 거리:', math.sqrt(current.data[1]**2 + current.data[2]**2))
    while current.link != head:
        current = current.link
        print(current.data[0], '편의점, 거리:', math.sqrt(current.data[1] ** 2 + current.data[2] ** 2))

def makeStoreList(storeData):
    global memory, head, current, pre

    node = Node()
    node.data = storeData
    memory.append(node)

    if head == None:
        head = node
        node.link = head
        return

    nodeX, nodeY = storeData[1:]
    nodeDist = math.sqrt(nodeX*nodeX + nodeY*nodeY)
    headX, headY = head.data[1:]
    headDist = math.sqrt(headX*headX + headY*headY)

    if headDist >= nodeDist:
        node.link = head # 헤드 앞에 삽입함. 그 다음은 아래와 같이 진행
        # head = node   # 이렇게 끝나면 안 되는 군. 그래서 AttributeError: 'NoneType' object has no attribute 'data' 가 중간에 나오게 되는 건가?
        last = head     # 아직 기존의 head임 : 이래야만 기존의 last를 찾을 수 있음
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
        if currDist >= nodeDist:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head    # 이걸 안 적었던 것도 오류의 문제였을 수도.

## 전역 변수
memory = []
head, current, pre = None, None, None

## 메인 코드
if __name__ == "__main__":

    storeList = []
    for i in range(ord('A'), ord('A')+10):
        name = chr(i)  # + ' 편의점' 이렇게 하면 실제 출력시 '편의점 , 거리: ~~' 이렇게 예시결과와 다른 띄어쓰기가 생기는 군.이러면 sep을 바꿔야 하고.
        xVal = random.randint(1, 100)
        yVal = random.randint(1, 100)
        data = (name, xVal, yVal)
        storeList.append(data)

    for data in storeList:
        makeStoreList(data)

    printStoreOrder(head)