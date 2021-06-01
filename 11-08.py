import os
##
def makeFileList(folderName):
    fnameAry = []
    for dirName, subDirList, fnames in os.walk(folderName):
        for fname in fnames:
            fnameAry.append(fname)
    return fnameAry

def insertionSort(ary):
    # n = len(ary)
    for end in range(1, len(ary)):  # 사이클은 앞의 2개(0과 1)부터, 하나씩 추가됨
        for current in range(end, 0, -1):  # 사이클 내에서는 뒤에서부터 확인해서, 큰 것을 앞으로 옮기는 작업을 함(내림차순)
            if ary[current-1] < ary[current]:  # 내림차순
                ary[current - 1], ary[current] = ary[current], ary[current-1]

    return ary

##
fileAry = []

##
fileAry = makeFileList('C:/Program Files/Common Files')
fileAry = insertionSort(fileAry)
print('파일명 역순 정렬 :', fileAry)