katok = ['다현', '정연', '쯔위', '사나', '지효']

def delete_data(position) :

    if position < 0 or position > len(katok) :
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    kLen = len(katok)

    for i in range(kLen-1, position-1, -1):
        katok[i] = None
        del(katok[i])

    ''' 
    # C나 자바 에서는 None 할 필요도 없이 비어있는데,
    # 파이썬 리스트는 자동으로 당겨지니까,
    # 어느 순간부터 리스트의 길이가 i보다 짧아지게 되서 오류.
    for i in range(position, kLen-1):
        katok[i] = None
        del(katok[i])
        print(katok)
    '''


delete_data(1)
print(katok)
delete_data(3)
print(katok)