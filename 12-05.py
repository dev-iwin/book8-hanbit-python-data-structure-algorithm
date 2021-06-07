##
def qSort(arr, start, end):
    if end <= start:
        return  # arr 여기선 왜 반환값이 없이 함수만 종료하지?

    # 오름차순
    low = start
    high = end

    pivot = arr[(low + high)//2]    # 중간 위치를 기준으로 작은 값은 왼, 큰 값은 오
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
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]

##
print('before :', dataAry)
# dataAry = 이거는 왜 대입이 필요 없지?
quickSort(dataAry)
print('after :', dataAry)