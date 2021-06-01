##
def insertionSort(ary):
    # n = len(ary)
    for end in range(1, len(ary)):  # 사이클은 앞의 2개(0과 1)부터, 하나씩 추가됨
        for current in range(end, 0, -1):  # 사이클 내에서는 뒤에서부터 확인해서, 작은 것을 앞으로 옮기는 작업을 함(오름차순)
            if ary[current-1] > ary[current]:
                ary[current - 1], ary[current] = ary[current], ary[current-1]

    return ary

##
dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

##
print('정렬 전 :', dataAry)
dataAry = insertionSort(dataAry)
print('정렬 후 :', dataAry)