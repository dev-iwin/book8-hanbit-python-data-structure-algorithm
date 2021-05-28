##
def notation(base, n):
    if n < base:
        print(numberChar[n], end='')
    else:
        notation(base, n//base)  # 앞자리 숫자로 올라가는 몫을 다시 notation하는 것임. 여기에 명령을 쓴 덕분에 앞자리 숫자가 먼저 출력됨
        print(numberChar[n % base], end='')

##
numberChar = [i for i in range(10)]
numberChar += ['A', 'B', 'C', 'D', 'E', 'F']

##
number = int(input('10진수 입력-->'))
print('\n2진수 :', end=' ')
notation(2, number)
print('\n8진수 :', end=' ')
notation(8, number)
print('\n16진수 :', end=' ')
notation(16, number)