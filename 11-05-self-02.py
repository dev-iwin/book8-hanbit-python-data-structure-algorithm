import random

def findInsertIdx(ary, data):
    findIdx = None
    for i in range(0, len(ary)):
        if ary[i] < data:       # 부등호 방향만 바꾸면 내림차순
            findIdx = i
            break
    if findIdx == None:
        return len(ary)
    else:
        return findIdx


##
before = [random.randint(0, 200) for _ in range(10)]
# for i in range(10):
#     before.append(random.randint(0, 200))
after = []

##
print('정렬 전 :', before)
for i in range(len(before)):
    data = before[i]
    insPos = findInsertIdx(after, data)
    after.insert(insPos, data)
print('정렬 후 :', after)