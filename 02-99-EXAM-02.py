## 가장 많이 나온 글자 my ver ##

originPoetStr = '''
나 보기가 역겨워 가실 때에는 말없이 고이 보내드리오리다
영변에 약산 진달래꽃 아름 따다 가실 길에 뿌리오리다
가시는 걸음 걸음 놓인 그 꽃을 사뿐히 즈려 밟고 가시옵소서
나 보기가 역겨워 가실 때에는 죽어도 아니 눈물 흘리오리다
'''

linePoetList = originPoetStr.splitlines()
# print(linePoetList)
sep = ''
linePoetStr = sep.join(linePoetList)
# print(linePoetStr)
noSpacePoetList = linePoetStr.split(' ')
# print(noSpacePoetList)
noSpacePoetStr = sep.join(noSpacePoetList)
# print(noSpacePoetStr)

countDic = {}


for i in noSpacePoetStr:
    if i not in countDic:
        count = 1
        countDic[i] = count
    else:
        countDic[i] += 1


print("----" * 10)
print("문자 빈도수 (4회 이상)")
print("----" * 10)

countList = list(countDic.items())
# print(countList)

for i in countList:
    if i[1] >= 4:
        print(i[0], i[1], sep = " --> ")
        # print("%s %d" (i[0], i[1]))  # 왜 안 되지??  # 이럴 필요는 없었구나
        # SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
        # TypeError: 'str' object is not callable


'''
1. 공백이나 개행은 제외 (split과 join)
2. 원문에서 한 글자를 추출 (for문과 문자열)
3. 1) 그 글자가 없으면 딕셔너리에 없으면 추가
   2) 그 글자가 있으면, 값을 +1
'''

