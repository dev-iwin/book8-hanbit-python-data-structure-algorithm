myList1 = []
myList2 = []
num = 12

for i in range(0, 4) :  # 4행
    for k in range(0, 3) :  # 3열
        myList2.append(num)
        num -= 1
    myList1.append(myList2)
    myList2 = []  # 초기화 까먹지 말자

for i in range(0, 4) :
    for k in range(0,3) :
        print("%5d" % myList1[i][k], end="  ")
        # 반환값을 숫자로 만들기 위해 포매팅 사용
    print("")  # 개행을 위한 코드구나

print("")
print("=====" * 10)
print("")

num2 = 12
myComprehension = [num2 for num2 in range(12, 0, -1)]
print(myComprehension)
# 2차원 리스트 컴프리헨션으로는, 값이 하나씩 감소하는 4행 3열 리스트를 못 만드나?