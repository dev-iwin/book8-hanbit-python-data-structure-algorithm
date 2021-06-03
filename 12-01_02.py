##
def bubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):   # n-1 ~ 1까지 돌면 사이클의 횟수이다.
        noChange = True     # changeYN = False로 해서 if not을 쓰는 방식을 이렇게 할 수 있다.
        for cur in range(0, end):   # end에 n-1이 들어가면 n-2까지 돌지면, cur+1과 비교하기에 n-1위치에 있는 마지막 요소까지 비교하게 된다!!!
            if ary[cur] > ary[cur+1]:
                ary[cur], ary[cur + 1] = ary[cur+1], ary[cur]
                noChange = False
        print('#사이클%d:' % (n-end), ary)  # for문 뒤에 나와야 사이클 처리 결과를 알 듯?
        if noChange:
            break
    return ary


##
dataAry = [50, 105, 120, 188, 150, 162, 168, 177]

##
print('before :', dataAry)
dataAry = bubbleSort(dataAry)
print('after :', dataAry)