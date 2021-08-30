global N
N = int(input('N: ')) # N <= 8 
  
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print (board[i][j], end = " ")
        print()

def isSafe(bo, row, column):
    # kiểm tra từ bên trái đến cột hiện tại xem đã có vị trị nào được đặt hay chưa 
    for i in range(column):
        if bo[row][i] == 1:
            return False
    # kiểm tra đường chéo trên bên trái
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if bo[i][j] == 1:
            return False
    # kiểm tra đường chéo dưới bên trái
    for i, j in zip(range(row, N, 1), range(column, -1, -1)):
        if bo[i][j] == 1:
            return False

    return True

# thử từng cột của board để đặt hậu
# mỗi cột sẽ thử tất cả các trường hợp có thể ở trong hàng để kiểm tra xem có hợp lệ hay không 

def solveNQUtil(bo, column):
    if column >= N:
        return True

    for i in range(N):
        if isSafe(bo,i, column):
            bo[i][column] = 1

            if solveNQUtil(bo, column + 1):
                return True
            bo[i][column] = 0

    return False


def solveNQ():
    board = [ [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0] ]
  
    if solveNQUtil(board, 0) == False:
        print ("Solution does not exist")
        return False
  
    printSolution(board)
    return True

solveNQ()