def findInsertIdx(ary, data):
    findIdx = None      # 없는 값 입력
    for i in range(0, len(ary)):
        if ary[i] > data:
            findIdx = i
            break
    if findIdx == None:     # 넣을 값보다 큰 기존 값이 없으면
        return len(ary)     # 제일 마지막 위치
    else:
        return findIdx

testAry = []
insPos = findInsertIdx(testAry, 55)
print('삽입할 위치 :', insPos)

testAry = [33, 77, 88]      # 기존의 배열은 이미 정렬이 완료된 상태인 것이 전제
insPos = findInsertIdx(testAry, 55)
print('삽입할 위치 :', insPos)

testAry = [33, 55, 77, 88]
insPos = findInsertIdx(testAry, 100)
print('삽입할 위치 :', insPos)
