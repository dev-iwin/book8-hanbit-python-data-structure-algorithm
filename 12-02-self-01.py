import random

##
def bubbleSort(ary):
    global count
    n = len(ary)
    for end in range(n-1, 0, -1):
        noChange = True
        for cur in range(0, end):   # 버블은 앞에서부터 2개씩 비교한다는 것을 기억하자
            count += 1
            if ary[cur] > ary[cur+1]:
                ary[cur], ary[cur + 1] = ary[cur+1], ary[cur]
                noChange = False
                #count += 1
        if noChange:
            break

    return ary


##
#dataAry = [random.randint(0, 200) for _ in range(20)]
dataAry = [158, 20, 119, 39, 66, 41, 124, 151, 168, 154]  # 왜 이 배열로 35회라는 숫자가 안 나오는 거지
count = 0   # 내림차순 비교 45회, 변경 32회 / 오름차순 비교 30회, 13회 변경

##
print('before :', dataAry)
dataAry = bubbleSort(dataAry)
print('after :', dataAry)
print('## %d회 비교로 정렬 완료' % count)