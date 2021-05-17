##
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        # print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        # print("스택이 비어있습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        # print("스택이 비어있습니다.")
        return None
    return stack[top]

def checkBracket(expr):
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            out = pop()
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else :
                return False
        else:
            pass
    if isStackEmpty():
        return True
    else:
        return False  # else를 안 쓰고 if문이랑 동일한 들여쓰기로 적으면 되는 거 아닌가? 이럴 땐 쓰네?

##
SIZE = 100
stack = [None for i in range(SIZE)]
top = -1

##
if __name__ == "__main__":

    exprAry = ['(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']

    for expr in exprAry:
        top = -1
        print(expr, '-->', checkBracket(expr))
