## 가장 많이 나온 글자 세기 book ver ##


## 전역 변수

poet = '''
나 보기가 역겨워 가실 때에는 말없이 고이 보내드리오리다
영변에 약산 진달래꽃 아름 따다 가실 길에 뿌리오리다
가시는 걸음 걸음 놓인 그 꽃을 사뿐히 즈려 밟고 가시옵소서
나 보기가 역겨워 가실 때에는 죽어도 아니 눈물 흘리오리다
'''

countDic = {}




## 메인 함수

if __name__ == '__main__':

    for ch in poet:
        if ch.isalpha():  # 공백과 개행은 여기서 제외됨
            if ch in countDic:
                countDic[ch] += 1
            else:
                countDic[ch] = 1

    print('원문', poet)
    print('-----' * 10)
    print('문자 빈도수(4회 이상)')
    print('-----' * 10)

    for key in countDic:  # 딕셔너리에서 기본으로 키가 추출됨
        if countDic[key] >= 4:
            print(key, '-->', countDic[key])  # 구분자가 아니라 문자열로 추가함