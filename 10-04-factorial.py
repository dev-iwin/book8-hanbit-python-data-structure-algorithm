# 반복문
factValue = 1
for n in range(10, 0, -1):
    factValue *= n
print('10!=', factValue)

print() # ==============

# 재귀 함수
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

print('10! =', factorial(5))

print() # ==============

def factorial2(num):
    if num <= 1:
        print('1! 반환')
        return 1
    print('%d * %d! 호출' % (num, num-1))
    # retVal = factorial2(num-1)
    print('%d * %d!(=%d) 반환' % (num, num-1, factorial2(num-1)))
    return num * factorial(num-1)

print('10! =', factorial2(5))

