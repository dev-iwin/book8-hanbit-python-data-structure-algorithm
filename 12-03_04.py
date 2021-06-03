##
def quickSort(ary):

    n = len(ary)
    if n <= 1:
        return ary

    pivot = ary[n//2]
    leftAry, midAry, rightAry = [], [], []

    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:  # 여기서 else가 아니라 elif를 써야, 기준값이 추가되지 않음
            rightAry.append(num)
        else:
            midAry.append(num)  # 얘는 재귀호출 필요 없음

    return quickSort(leftAry) + midAry + quickSort(rightAry)   # 한 줄, 그것도 reture에 재귀호출을 두번을 해도 된단 말이야?!

##
dataAry = [120, 120, 188, 150, 168, 50, 50, 162, 105, 120, 177, 50]

##
print('before :', dataAry)
dataAry = quickSort(dataAry)
print('after :', dataAry)