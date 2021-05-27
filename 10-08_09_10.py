print('## 10-08 N제곱 계산 시각화 ##')

tab=''
def myPow(x, n):
    global tab
    tab += '  '
    if n == 0:
        return 1
    print(tab + '%d*%d^(%d-%d)' % (x, x, n, 1))
    return x * myPow(x, n-1)

print('2^4')
print('답 :', myPow(2, 4))


print()
print('## 10-09 배열 합 계산 ##')

import random
def arySum(arr, n):
    if n == 0:
        return ary[0]
    return arr[n] + arySum(arr, n-1)

ary = [random.randint(0, 255) for _ in range(random.randint(10, 20))]

print(ary)
print('합계 : ', arySum(ary, len(ary)-1))


print()
print('## 10-10 피보나치 수 구현 ##')

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

print('피보나치 수 :', end=' ')
for i in range(20):
    print(fibo(i), end=' ')