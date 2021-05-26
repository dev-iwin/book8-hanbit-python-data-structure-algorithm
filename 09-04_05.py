##
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print('   ', end=' ')
    for v in range(g.SIZE):
        print(nameAry[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(nameAry[row], end=' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end='  ')
        print()
    print()

def findVertex(g, findVtx):
    stack = []
    visitedAry = []

    current = 0
    stack.append(current)
    visitedAry.append(current)

    while (len(stack) != 0):
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0:
                if vertex in visitedAry:
                    pass
                else:
                    next = vertex
                    break
        if next != None:
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:
            current = stack.pop()

    if findVtx in visitedAry:
        return True
    else:
        return False


## 전역 변수
G1 = None
nameAry = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5


## 메인 코드
gSize = 6
G1 = Graph(gSize)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15;
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50;
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12;
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30;
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25;
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25;

print('## 자전거 도로 건설을 위한 전체 연결도')
printGraph(G1)

## 가중치 간선 목록
edgeAry = []
for i in range(gSize):
    for k in range(gSize):
        if G1.graph[i][k] != 0:
            edgeAry.append([G1.graph[i][k], i, k])

from operator import itemgetter
# 이걸 왜 여기서 임포트 하는 걸까? 쓰기 직전이기 때문에?

edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=True)

newAry = []
for i in range(0, len(edgeAry), 2):
    newAry.append(edgeAry[i])

index = 0  # newAry의 인덱스 번호
while (len(newAry) > gSize-1):  # len(newAry) != (gSize-1)  # 이렇게 해도 될 것 같기도 한데..
    start = newAry[index][1]
    end = newAry[index][2]
    saveCost = newAry[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    startYN = findVertex(G1, start)
    endYN = findVertex(G1, end)

    if startYN and endYN:
        del(newAry[index])
    else:
        G1.graph[start][end] = saveCost
        G1.graph[end][start] = saveCost
        index += 1

print('## 최소 비용의 자전거 도로 연결도')
printGraph(G1)