from operator import itemgetter

##
def makeIndex(ary, col):
    beforeAry = []
    index = 0
    for data in ary:
        beforeAry.append((data[col], index))
        index += 1

    sortedAry = sorted(beforeAry, key=itemgetter(0))
    return sortedAry

def bookSearch(ary, fData):
    pos=-1
    start = 0
    end = len(ary)-1

    while start <= end:
        mid = (start + end) // 2
        if fData == ary[mid][0]:
            return ary[mid][1]
        elif fData > ary[mid][0]:
            start = mid + 1
        else:
            end = mid - 1

    return col

##
bookAry = [['어린왕자', '쌩떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이']
           , ['신곡', '단테'], ['돈키호테', '세르반테스'], ['동물농장', '조지오웰']
           , ['데미안', '헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅']]
nameIndex = []
authIndex = []

##
nameIndex = makeIndex(bookAry, 0)
print('# 도서명 색인표 :', nameIndex)
authIndex = makeIndex(bookAry, 1)
print('# 도서명 색인표 :', authIndex)

findName = '신곡'
findPos = bookSearch(nameIndex, findName)
if findPos != -1:
    print(findName, '의 작가 :', bookAry[findPos][1])
else:
    print('없음')


findName = '괴테'
findPos = bookSearch(authIndex, findName)
if findPos != -1:
    print(findName, '의 저서 :', bookAry[findPos][0])
else:
    print('없음')