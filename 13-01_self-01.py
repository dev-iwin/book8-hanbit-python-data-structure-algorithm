##
def seqSearch(ary, fData):
    pos = -1
    size = len(ary)
    print('비교한 데이터 :', end=' ')
    for i in range(size):
        print(ary[i], end=' ')
        if ary[i] == fData:
            pos = i
            break
    print()
    return pos

##
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]
findData = 0  # 입력 안 했을 때를 대비한 건가?

##
findData = int(input('찾을 값 : '))
print('배열 :', dataAry)

position = seqSearch(dataAry, findData)
if position == -1:
    print(findData, '없음')
else:
    print(findData, '의 위치는', position)



## ========================================


## self-01
def seqSearch(ary, fData):
    pos = []
    size = len(ary)

    for i in range(size):
        print(ary[i], end=' ')
        if ary[i] == fData:
            pos.append(i)

    print()
    return pos

##
dataAry = [188, 50, 150, 168, 50, 162, 105, 120, 177, 50]
findData = 0

##
findData = 50
print('배열 :', dataAry)

position = seqSearch(dataAry, findData)
if position == -1:
    print(findData, '없음')
else:
    print(findData, '의 위치는', position)