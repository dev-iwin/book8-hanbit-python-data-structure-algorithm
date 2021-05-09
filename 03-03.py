katok = ['다현', '정연', '쯔위', '사나', '지효']

def delete_data(position) :

    if position < 0 or position > len(katok) :
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    kLen = len(katok)
    katok[position] = None

    '''
    for i in range(position, kLen - 1) :
        katok[i] = katok[i+1]
        katok[i+1] = None  # 이것도 되는데, 이렇게 하면 
        # 마지막 반복에 katok[kLen - 1 + 1] = None 이 되면서
        # 마지막 칸을 비운다는 의미가 직관적이지 않아서 그런가?
    '''
    for i in range(position + 1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[kLen - 1])


print(katok)
delete_data(1)
print(katok)
delete_data(3)
print(katok)