## 2차원 배열 중앙값 찾기
def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for current in range(end, 0, -1):
            if ary[current-1] > ary[current]:
                ary[current-1], ary[current] = ary[current], ary[current-1]
    return ary

##
ary2 = [[55, 33, 250, 44],
       [88, 1, 67, 23],
       [199, 222, 38, 47],
       [155, 145, 20, 99]]
ary1 = []   # 빈 배열 안 쓰는 방법 없을까?

##
for i in range(len(ary2)):
    for k in range(len(ary2[i])):
        ary1.append(ary2[i][k])

print('전 :', ary1)
ary1 = insertionSort(ary1)
print('후 :', ary1)

print('중앙값 :', ary1[len(ary1)//2])