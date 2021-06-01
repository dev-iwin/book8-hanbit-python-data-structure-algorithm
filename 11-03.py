##
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1) :  # 사이클 횟수
        minIdx = i  # 이번 사이클에서 비교해야 할 값들 중에 제일 앞에 있는 값
        for k in range(i+1, len(ary)):   # i 다음 값부터 끝까지 비교하기
            if ary[minIdx] > ary[k]:
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

    return ary

##
dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

##
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)