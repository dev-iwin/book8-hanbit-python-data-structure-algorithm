import random

##
def isStackFull():
    global SIZE, stack, top
    if top >= SIZE:
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top

    if isStackFull():
        # print("Full")
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top

    if isStackEmpty():
        # print("Empty")
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top

    if isStackEmpty():
        # print("Empty")
        return
    return stack[top]

##
SIZE = 10
stack = [None for i in range(SIZE)]
top = -1

##
if __name__ == '__main__':
    stoneAry = ['빨강', '파랑', '초록', '노랑', '보라', '주황']
    random.shuffle(stoneAry)

    print('과자집에 가는 길 : ', end='')
    for stone in stoneAry:
        push(stone)
        print(peek() + '-->', end='')   # 책 : peek()을 안 쓰고, 그냥 stone으로 넣음
    print("과자집")

    print('우리집에 오는 길 : ', end='')
    # for stone in range(len(stoneAry)):
    # 다음이 책 코드
    while True:             # while문으로 추출하면 맨 마지막엔 pop()함수 에서 isStackEmpty가 True일 때 실행할 명령이 있으면 실행되는 군.
        stone = pop()
        if stone == None:   # 여기선 top == -1 이나, isStackEmpty를 안 쓰나?
            break
        print(stone + '-->', end='')
    print("우리집")