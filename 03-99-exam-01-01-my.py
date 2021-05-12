## 함수 선언
def insert_data(friend, count):
    new_data = (friend, count)
    katok.append(None)
    kLen = len(katok)-1

    for i in range(kLen):
        if count >= katok[i][1]:                    # 기능1 : 위치
            position = i
            for k in range(kLen, position, -1):     # 기능2 : 삽입
                katok[k] = katok[k-1]
                katok[k-1] = None
            katok[position] = new_data
            break
                                                    # for문 안에 있던 if를, 책처럼 밖에 두는 것으로 수정함
    if count < katok[kLen-1][1]:                    # 기능1 : 위치
        katok[kLen] = new_data                      # 기능2 : 삽입
                                                    # 책처럼 기능 1과 2를 명확히 분리하는 것이 나을 듯함
    print(katok)


## 전역 변수 부분
katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]


## 메인 코드 부분
if __name__ == '__main__':

    while True:
        friend = input('추가할 친구 --> ')
        count = int(input('카톡 횟수 --> '))
        insert_data(friend, count)