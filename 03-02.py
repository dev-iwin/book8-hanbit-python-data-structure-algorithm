katok = ['다현', '정연', '쯔위', '사나', '지효']

def insert_data(position, friend) :
    if position < 0 or position > len(katok) :
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return


    katok.append(None)  # 빈칸 추가 = 길이 증가
    kLen = len(katok)   # 1 증가된 길이가 반환됨


    for i in range(kLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

print(katok)
insert_data(2, '솔라')
print(katok)
insert_data(6, '문별')
print(katok)