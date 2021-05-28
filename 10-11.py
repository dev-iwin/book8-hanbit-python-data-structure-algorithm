##
def palindrom(pStr):
    if len(pStr) <= 1:
        return True
    if pStr[0] != pStr[-1]:
        return False
    return palindrom(pStr[1:len(pStr)-1])  # return 없으면 안 됨

##
strAry = ['reaver', 'kayak', 'Borrow or rob', '주유소의 소유주', '야 너 이번 주 주번이 너야', '살금 살금']

## 메인 코드 : 재귀 중에 반복할 필요 없는 작업들
for testStr in strAry:
    print(testStr, end='-->')
    testStr = testStr.lower().replace(' ', '')
    if palindrom(testStr):
        print('O')
    else:
        print('X')