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
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top

    if isStackEmpty():
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top

    if isStackEmpty():
        return
    return stack[top]

##
SIZE = 100
stack = [None for i in range(SIZE)]
top = -1

##
if __name__ == '__main__':

    with open("진달래꽃.txt", 'r', encoding='UTF8') as rfp:
        linesAry = rfp.readlines()   # 행별로 배열(파이썬의 리스트)에 담기는 군

    print("----- 원본 -----")
    for line in linesAry:
        print(line, end='')

        for ch in line:
            push(ch)    # 이 두 줄이면 되는데, 책은 왜 그렇게 한 거지?

    print()
    print('----- 거꾸로 -----')
    while True:
        ch = pop()
        if ch == None:
            break
        print(ch, end='')