##
def findMinIdx(ary):
    minIdx = 0      # 첫번째 값을 가리킴
    for i in range(1, len(ary)):   # 두번째 값부터 끝까지 비교하기
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx

##
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

##
print('정렬 전 -->', before)
for _ in range(len(before)):
    minPos = findMinIdx(before)
    after.append(before[minPos])
    del before[minPos]  # 여기서 삭제해야, 그 다음 반복시에 최솟값과 그 위치가 바뀌는 군
print('정렬 후 -->', after)