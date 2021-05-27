##
def openBox(count):
    # global count
    print('open a box')
    count -= 1
    if count == 0:
        print('put the ring in the box and start closing(returning)')
        return
    openBox(count)
    print('close a box')


##
# count = 10

##
openBox(10)

## 전역변수와 글로벌 예약어 없는 함수 만들어 봄