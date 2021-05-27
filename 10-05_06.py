print('## 우주선 발사 카운트')
print()

def countDown(n):
    if n == 0:
        print('발사!')
    else:
        print(n)
        countDown(n-1)

countDown(5)
print()

print('## 별표 출력')
print()

def printStar(n):
    if n > 0:
        printStar(n-1)  # 큰 숫자부터 하나씩 작아지는데, 출력은 작은 수부터 큰 수로 늘어나야할 때, 실행할 명령문 앞에 재귀함수!!!
        print('*' * n)

printStar(5)