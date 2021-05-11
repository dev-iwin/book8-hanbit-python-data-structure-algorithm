## 뮤터블한 리스트 탐구 ##

print("===" * 5 + "뮤터블한 리스트 탐구" + "===" * 5)

oneLotto1 = [1, 2, 3]
allLotto1 = [[1, 2, 3]]
if oneLotto1 not in allLotto1:
    allLotto1.append(oneLotto1)
    print("다른 데이터를 가르킴")
else:
    print("같은 데이터를 가르킴")  # 같다고 나옴

oneLotto2 = []
allLotto2 = [oneLotto2]
# oneLotto2 = [1, 2, 3, 4]  # 다르다고 나옴. 새로운 데이터를 생성한 샘
for i in range(1,5):
    oneLotto2.append(i)  # 같다고 나옴. 기존의 데이터를 수정한 셈(뮤터블)
if oneLotto2 not in allLotto2:
    allLotto2.append(oneLotto2)
    print("다른 데이터를 가르킴")
else:
    print("같은 데이터를 가르킴")


a = [1, 2]
b = a
a.append(3)
print(b)  # a와 함께 변함