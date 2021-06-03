import random

##
def quickSort(ary):
    global count

    n = len(ary)
    if n <= 1:
        return ary

    pivot = ary[n//2]
    leftAry, rightAry = [], []

    for num in ary:
        count += 1
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)

    return quickSort(leftAry) + [pivot] + quickSort(rightAry)

##
dataAry = [31, 49, 175, 33, 103, 76, 63, 151, 166, 25]
count = 0

##
print('before :', dataAry)
dataAry = quickSort(dataAry)
print('after :', dataAry)
print(count, '회 비교로 정렬 완료')