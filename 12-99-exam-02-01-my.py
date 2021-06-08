import random
import time

##
def bubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        noChange = True
        for cur in range(0, end):
            if ary[cur] > ary[cur+1]:
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                noChange = False
        if noChange:
            break
    return ary

def qSort(arr, start, end):
    if end <= start:
        return

    low = start
    high = end

    pivot = arr[(low + high)//2]
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
tempAry = [random.randint(10000, 99999) for _ in range(1000000)]
tempAry.sort()

randomPos = random.randint(0, len(tempAry)-1)
print('데이터 개수 : 1000000 개')
print('삽입된 위치 :', randomPos)

bubAry = tempAry[:]
quickAry = tempAry[:]

start = time.time()
bubbleSort(bubAry)
end = time.time()
print('버블 시간 :', end-start)

start = time.time()
quickSort(quickAry)
end = time.time()
print('퀵 시간 :', end-start)
