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
        elif ary[i] > fData:
            break
    print()
    return pos

##
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]
findData = 0  # 입력 안 했을 때를 대비한 건가?

##
dataAry.sort()
findData = int(input('찾을 값 : '))
print('배열 :', dataAry)
position = seqSearch(dataAry, findData)
if position == -1:
    print(findData, '없음')
else:
    print(findData, '의 위치는', position)
