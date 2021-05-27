def addNumber(num):
    if num <= 1:
        return 1
    return num + addNumber(num-1)

print(addNumber(10))

## ======== self 10-1 ============

firstNum = int(input('숫자1 --> '))
secondNum = int(input('숫자2 --> '))

## ===============================

def addNumber2(num1, num2):
    # 작은 수부터 큰 수로 커지는 방식
    if num1 == num2:
        return num1
    elif num1 < num2:
        return num1 + addNumber2(num1+1, num2)
    else:
        return num2 + addNumber2(num1, num2+1)

print(addNumber2(firstNum, secondNum))

## ===============================

def addNumber3(num1, num2):
    # 큰 수부터 작은 수로 커지는 방식
    if num1 == num2:
        return num1
    elif num1 > num2:
        return num1 + addNumber2(num1-1, num2)
    else:
        return num2 + addNumber2(num1, num2-1)

print(addNumber3(firstNum, secondNum))