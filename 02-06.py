myList = [30, 10, 20]
print("현재 리스트 : %s" % myList)
# 리스트는 문자열로 취급되는구나. 문자열도 결국 문자로 리스트 만든 거긴 하니까.

myList.append(40)
print("append(40) 후의 리스트 : %s" % myList)

print("pop() 으로 추출한 값 : %s" % myList.pop())
print("pop() 후의 리스트 : %s" % myList)
# 자료구조와 알고리즘을 공부하다보면, .pop()이 왜 존재하고 기본적인 함수인지 깨달을 수 있겠지? 언제 쓰면 유용한지 궁금

myList.sort()  # 오름차순으로 정렬
print("sort() 후의 리스트 : %s" % myList)

myList.reverse()  # 내림차순으로 정렬
print("reverse() 후의 리스트 : %s" % myList)

print("20 값의 위치 : %d" % myList.index(20))  # 위치

myList.insert(2, 222)  # 지정한 위치에 삽입
print("insert(2, 222) 후의 리스트 : %s" % myList)

myList.remove(222)  # 지정한 값을 찾아서 삭제 (여러 개면 첫 번째만)
print("remove(222) 후의 리스트 : %s" % myList)

myList.extend( [77 , 88, 77] )  # 리스트를 연결(더하기 연산과 같은 효과)
print("extend([77, 88, 77]) 후의 리스트 : %s" % myList)

print("77 값의 개수 : %d" % myList.count(77))  # 개수 세기
