## 리스트 탐구 ##

print("=====" * 5 + "리스트 탐구" + "=====" * 5)

oneLotto1 = [1, 2, 3]
allLotto1 = [[1, 2, 3],]

print(id(oneLotto1))
print(id(allLotto1[0]))
# 두 아이디 다름에도 불구하고, 아래 조건식에서는 같은 내용이라고 확인됨

if oneLotto1 not in allLotto1:
    print("다른 데이터를 갖음")
else:
    print("같은 데이터를 갖음")  # 같다고 나옴

####################################

oneLotto2 = []
allLotto2 = [oneLotto2]

for i in range(1, 5):
    oneLotto2.append(i)  # 같다고 나옴. 기존의 데이터를 수정한 샘

print(id(oneLotto2))
print(id(allLotto2[0]))

# oneLotto2 = [1, 2, 3, 4]  # 다르다고 나옴. 새로운 데이터를 생성한 샘

if oneLotto2 not in allLotto2:
    print("다른 데이터를 가르킴")
else:
    print("같은 데이터를 가르킴")

######################################

a = [1, 2]
b = a
a.append(3)
print(b)  # a와 함께 변함


######################################

