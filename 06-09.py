import webbrowser
import time

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
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 비어있습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 비어있습니다.")
        return None
    return stack[top]

##
SIZE = 100
stack = [None for i in range(SIZE)]
top = -1

##
if __name__ == "__main__":
    urls = ['naver.com', 'daum.net', 'nate.com']
    # 왜 얘는 전역번수 아니고 메인코드에 넣었을까, 그리고 프로토콜은 왜 밑에 쓴 걸까? 반복방지? 그리고 왜 http's'가 아닌 걸까?
    for url in urls:
        push(url)
        webbrowser.open('http://' + url)
        print(url, end='-->')
        time.sleep(1)

    print("방문 종료")
    time.sleep(4)

    while True:
        url = pop()
        if url == None:
            break
        webbrowser.open('http://' + url)
        print(url, end='-->')
        time.sleep(1)

    print("방문 종료")
