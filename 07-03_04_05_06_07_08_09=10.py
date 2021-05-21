##
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        return False
    elif (rear == SIZE-1) and (front == -1):
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("Full")
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("Empty")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("Empty")
        return None
    return queue[front+1]

##
SIZE = int(input("큐의 크기를 지정하세요 --> "))
queue = [None for i in range(SIZE)]
front = rear = -1

##
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 택1 --> ")

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input('입력할 데이터 --> ')
            enQueue(data)
            print('큐 상태 : ', queue)
        elif select == 'E' or select == 'e':
            data = deQueue()
            print('추출된 데이터 : ', data)
            print('큐 상태 : ', queue)
        elif select == 'V' or select == 'v':
            data = peek()
            print('확인된 데이터 : ', data)
            print('큐 상태 : ', queue)
        else:
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 택1 --> ")

    print("프로그램 종료")