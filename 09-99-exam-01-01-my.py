## 순회해서 숫자 제일 큰 요소 출력하기인 셈
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print('         ', end=' ')
    for i in range(gSize):              # v 라고 했음. 정점에 대응하는 문자열을 출력하기 위함이라 v인듯
        name = storeAry[i][0]           # 반환값을 담을 변수 필요 없고, 문자열도 포맷을 이용해 정렬
        print(name.center(8), end=' ')  # print('%9s' % storeAry[i][0], end=' ')
    print()
    for i in range(g.SIZE):             # row 라고 했음
        name = storeAry[i][0]
        print(name.rjust(8), end=' ')
        for k in range(g.SIZE):         # col 이라고 했음
            edge = g.graph[i][k]
            print('%6d' % edge, end='   ')  # print('%8d' % g.graph[i][k], end=' ')
        print()
    print()


## 변수
G1 = Graph(5)
storeAry = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4


## 메인
gSize = 5
G1 = Graph(gSize)
G1.graph[GS25][CU] = 1; G1.graph[GS25][Seven11] = 1;
G1.graph[CU][GS25] = 1; G1.graph[CU][Seven11] = 1; G1.graph[CU][MiniStop] = 1;
G1.graph[Seven11][GS25] = 1; G1.graph[Seven11][CU] = 1; G1.graph[Seven11][MiniStop] = 1;
G1.graph[MiniStop][CU] = 1; G1.graph[MiniStop][Seven11] = 1; G1.graph[MiniStop][Emart24] = 1;
G1.graph[Emart24][MiniStop] = 1;

print('## 편의점 그래프')
printGraph(G1)

## 편의점 다 방문해보고 재고 제일 많은 편의점 출력하기 : 큰 숫자 찾으면 그 스토어 가리키게 하기
stack = []
visitedAry = []

current = 0
maxStore = current
maxCount = storeAry[current][1]
stack.append(current)
visitedAry.append(current)

while (len(stack) != 0):
    next = None
    for vertex in range(gSize):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break
    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
        if storeAry[current][1] > maxCount:
            maxStore = current
    else:
        current = stack.pop()

print('허니버터칩 최대 보유 편의점(개수) -->', storeAry[maxStore][0], '(', storeAry[maxStore][1], '개)')