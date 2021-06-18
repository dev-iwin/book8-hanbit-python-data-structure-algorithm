##
def knapsack():
    print('## 메모이제이션 배열')
    array = [[0 for _ in range(maxWeight + 1)] for _ in range(rowCount + 1)]
    for row in range(1, rowCount + 1):
        print(row, '개 :', end='  ')
        for col in range(1, maxWeight + 1):
            if weight[row] > col:
                array[row][col] = array[row - 1][col]
            else:
                value1 = money[row] + array[row - 1][col - weight[row]]
                value2 = array[row - 1][col]
                array[row][col] = max(value1, value2)
            print('%3d' % array[row][col], end='')
        print()
    return array[rowCount][maxWeight]



##
maxWeight = 7
rowCount = 4
weight = [0, 6, 4, 3, 5]
money = [0, 13, 8, 6, 12]

##
maxValue = knapsack()
print()
print('배낭에 담을 수 있는 보석의 최대 가격 :', maxValue, '억원')


## self-01
weight = [0, 5, 3, 6, 4]
money = [0, 12, 6, 13, 8]

maxValue = knapsack()
print()
print('배낭에 담을 수 있는 보석의 최대 가격 :', maxValue, '억원')
