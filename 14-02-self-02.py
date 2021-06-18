##
def growRich():
    memo = [[0 for _ in range(COL)] for _ in range(ROW)]
    memo[0][0] = dangerMaze[0][0]

    rowSum = memo[0][0]
    for i in range(1, ROW):
        rowSum += dangerMaze[0][i]
        memo[0][i] = rowSum

    colSum = memo[0][0]
    for i in range(1, COL):
        colSum += dangerMaze[i][0]
        memo[i][0] = colSum

    for row in range(1, ROW):
        for col in range(1, COL):
            if (memo[row][col-1]) < (memo[row-1][col]):
                memo[row][col] = memo[row][col-1] + dangerMaze[row][col]
            else:
                memo[row][col] = memo[row-1][col] + dangerMaze[row][col]

    return memo[ROW-1][COL-1]


##
ROW, COL = 5, 5
dangerMaze = [[1, 4, 4, 2, 2],
              [1, 3, 3, 0, 5],
              [1, 2, 4, 3, 0],
              [3, 3, 0, 4, 2],
              [1, 3, 4, 5, 3]]

##
miniDanger = growRich()
print('위험미로에서 만난 위험요소 최소 개수 :', miniDanger)