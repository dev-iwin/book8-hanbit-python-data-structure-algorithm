##
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print('   ', end=' ')
    for v in range(g.SIZE):
        print('%s'.center(3) % cityAry[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(cityAry[row], end=' ')
        for col in range(g.SIZE):
            print('%4d' % g.graph[row][col], end=' ')
        print()
    print()

def findVertex(g, findVtx):
    stack = []
    visitedAry = []

    current = 0
    stack.append(current)
    visitedAry.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(g.SIZE):
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

##
G1 = None
cityAry = ['서울', '뉴욕', '런던', '북경', '방콕', '파리']
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5

##
gSize = 6
G1 = Graph(gSize)
G1.graph[서울][뉴욕] = 80; G1.graph[서울][북경] = 10;
G1.graph[뉴욕][서울] = 80; G1.graph[뉴욕][북경] = 40; G1.graph[뉴욕][방콕] = 70;
G1.graph[런던][방콕] = 30; G1.graph[런던][파리] = 60;
G1.graph[북경][서울] = 10; G1.graph[북경][뉴욕] = 40; G1.graph[북경][방콕] = 50;
G1.graph[방콕][뉴욕] = 70; G1.graph[방콕][런던] = 30; G1.graph[방콕][북경] = 50; G1.graph[방콕][파리] = 20;
G1.graph[파리][런던] = 60; G1.graph[파리][방콕] = 20;

print('해저 케이블 계획도')
printGraph(G1)
# print(findVertex(G1, 5))

## 가중치 간선 목록
edgeAry = []  # [가중치, 출발도시, 도착도시] 넣을 배열
for row in range(gSize):
    for col in range(gSize):
        if G1.graph[row][col] != 0:
            edgeAry.append([G1.graph[row][col], row, col])

from operator import itemgetter
edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=False)
# print(edgeAry)

newAry = []
for i in range(0, len(edgeAry), 2):
    newAry.append(edgeAry[i])
# print(newAry)

index = 0   # newAry 에서 사용한 인덱스 넘버
while len(newAry) > gSize-1 :
    start = newAry[index][1]
    end = newAry[index][2]
    cost = newAry[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    startYN = findVertex(G1, start)
    endYN = findVertex(G1, end)

    if startYN and endYN:
        del newAry[index]
    else:
        G1.graph[start][end] = cost
        G1.graph[end][start] = cost
        index += 1

print('## 가장 빠른 해저 케이블 연결도')
printGraph(G1)