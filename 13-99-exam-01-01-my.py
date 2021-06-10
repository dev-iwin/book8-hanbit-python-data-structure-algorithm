import random
##
def binSearch(ary, fData):
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

##
dataAry = ['빙바', '레쓰비', '츄파춥스', '도시락', '삼다수', '콜라', '삼김']
sellAry = [random.choice(dataAry) for _ in range(20)]

##
print('오늘 판매된 전체 물건(중복O, 정렬X) :', sellAry)
sellAry.sort()
print('오늘 판매된 전체 물건(중복O, 정렬O) :', sellAry)
sellProduct = list(set(sellAry))
print('오늘 판매된 물건의 종류(중복x) :', sellProduct)

countList = []
for product in sellProduct:
    count = 0
    pos = 0
    while pos != -1:
        pos = binSearch(sellAry, product)
        if pos != -1:
            count += 1
            del sellAry[pos]    # 이전에 찾은 값을 삭제해가며, 새로 카운트 하는군
    countList.append((product, count))  # 반복이 다 끝난 후 추가

print()
print('계산 결과 :', countList)