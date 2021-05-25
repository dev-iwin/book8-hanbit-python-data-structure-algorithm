##
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

##
G1 = None
stack = []
visitedAry = []

##
gSize = 4
G1 = Graph(gSize)
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(gSize):
    for col in range(gSize):
        print(G1.graph[row][col], end=' ')
    print()
print()

## 깊이 우선 탐색
current = 0
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
                break  # for문 탈출

    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()

print('오름차순 방문 : ', end='')
for i in visitedAry:
    print(chr(ord('A')+i), end=' ')