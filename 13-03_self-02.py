##
def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary) - 1
    global count
    while start <= end:
        count += 1
        mid = (start+end)//2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid+1
        else:
            end = mid-1

    return pos

##
dataAry = [50, 60, 105, 120 ,150, 160, 162, 168, 177, 188]
findData = 162
count = 0

##
print('배열 :', dataAry)
position = binSearch(dataAry, findData)
if position == -1:
    print('없음')
else:
    print(findData, '의 위치 :', position)


## =================
## self-02
print()
print()

import random

selfAry = [random.randint(0, 100000) for _ in range(100000)]
testNum = random.randint(0, 100000)
location = binSearch(selfAry, testNum)
if location == -1:
    print('없음')
else:
    print(testNum, '의 위치 :', location)
print(count, '번 검색')