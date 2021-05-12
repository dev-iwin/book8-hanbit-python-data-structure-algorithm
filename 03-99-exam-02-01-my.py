## 함수 선언 부분
def printPoly(p_x):
    polyStr = "P(x) = "
    for i in range(len(p_x[1])):
        if p_x[1][i] > 0:
            polyStr += "+"  # + str(p_x[1][i]) + "x^" + str(p_x[0][i])
        polyStr += str(p_x[1][i]) + "x^" + str(p_x[0][i]) + " "
    print(polyStr)

def calcPoly(p_x):
    hap = 0                                         # 책에서는 retValue 라고 명명
    xVal = int(input("x의 값은? --> "))              # 책에서는 메인 코드로 작성하고 또 하나의 인수로 넘김
    for i in range(len(p_x[1])):
        hap += p_x[1][i] * (xVal ** p_x[0][i])      # 영어 : 계수는 coefficient, 차수는 degree
    print(hap)

''' 책에는 각 함수마다 return을 하고, 메인 코드에서 직접 print하더라. 왜?'''
## 전역 변수 부분
px = [[300, 20, 0], [7, -4, 5]]

## 메인 코드 부분
if __name__ == '__main__':
    printPoly(px)
    calcPoly(px)