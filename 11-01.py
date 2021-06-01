def findMinIdx(ary):
    minIdx = 0      # 첫번째 값을 가리킴
    for i in range(1, len(ary)):   # 두번째 값부터 끝까지 비교하기
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx

testAry = [55, 88, 33, 77]
minPos = findMinIdx(testAry)
print('최솟값 -->', testAry[minPos])


def findMaxIdx(ary):
    maxIdx = 0      # 첫번째 값을 가리킴
    for i in range(1, len(ary)):   # 두번째 값부터 끝까지 비교하기
        if ary[maxIdx] < ary[i]:
            maxIdx = i
    return maxIdx

testAry2 = [55, 88, 33, 77]
maxPos = findMaxIdx(testAry2)
print('최댓값 -->', testAry2[maxPos])