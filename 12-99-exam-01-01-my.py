import random
import time

##
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIndex = i
        for k in range(i+1, n):
            if ary[minIndex] > ary[k]:
                minIndex = k
        temp = ary[i]
        ary[i] = ary[minIndex]
        ary[minIndex]= temp

    return ary


##
def qSort(arr, start, end):
    if end <= start:
        return

    low = start
    high = end

    pivot = arr[(low+high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low+1, high-1

    mid = low

    qSort(arr, start, mid-1)
    qSort(arr, mid, end)

def quickSort(ary):
    qSort(ary, 0, len(ary)-1)



##
countAry = [1000, 10000, 12000, 15000]

for count in countAry:
    tempAry = [random.randint(10000, 99999) for _ in range(count)]
    selectAry = tempAry[:]
    quickAry = tempAry[:]

    print('데이터 수 : %d 개' % count)

    start = time.time()  # 시작 시간
    selectionSort(selectAry)
    end = time.time()  # 완료 시간
    print('선택정렬 :', end-start)

    start = time.time()
    quickSort(quickAry)
    end = time.time()
    print('선택정렬 :', end - start)

    print()

    # count *= 5
