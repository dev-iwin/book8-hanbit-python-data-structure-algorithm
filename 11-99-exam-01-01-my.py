## 조 편성
def selectionSort(ary):
    for i in range(0, len(ary)-1):  # 맨 마지막은 돌 필요가 없을 테니까. 사이클의 개수도 그렇고.
        minPos = i
        for k in range(i+1, len(ary)):
            if ary[minPos][1] > ary[k][1]:
                minPos = k
        tmp = ary[minPos]
        ary[minPos] = ary[i]
        ary[i] = tmp
    return ary

##
dataAry = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

## 정렬 후 매칭할 필요 없이, 그냥 뽑아서 해도 될 것 같은데. 정렬 예제니까..
print('전 :', dataAry)
dataAry = selectionSort(dataAry)
print('후 :', dataAry)

print('## 성적별 조 편성 ##')
for j in range(len(dataAry)//2):
    print('%s : %s' % (dataAry[j][0], dataAry[len(dataAry)-1-j][0]))