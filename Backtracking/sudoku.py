board = [
  [7,8,0,4,0,0,1,2,0],
  [6,0,0,0,7,5,0,0,9],
  [0,0,0,6,0,1,0,7,8],
  [0,0,7,0,4,0,2,6,0],
  [0,0,1,0,5,0,9,3,0],
  [9,0,4,0,6,0,0,0,5],
  [0,7,0,3,0,0,0,1,2],
  [1,2,0,0,0,7,4,0,0],
  [0,4,9,2,0,6,0,0,7]
]


def find_zero(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def solve(bo):
    find = find_zero(bo)
    if not find:
        return True 
    else:
        row, column = find 
    
    for i in range(1, 10):
        if check(bo, i, (row, column)):
            bo[row][column] = i 
            if solve(bo):
                return True
            bo[row][column ] = 0
    return False


def check(bo, num, pos):
    # kiểm tra xem giá trị tại vị trí pos đã tồn tại trong hàng hay chưa
    for i in range(0,9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    # kiểm tra xem giá trị tại vị trí pos có trong cột hay chưa
    for  i in range(0, 9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # kiểm tra trong box 3 * 3 của vị trí hiện tại xem có giá trị đó hay chưa 
    x = pos[0] // 3
    y = pos[1] // 3

    for i in range(x * 3, x * 3 + 3):
        for j in range(y * 3, y * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('---------------------')
        for j in range(len(bo[i])):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')
    print('\n')

print('--------GAME SUDOKU-------\n')
print_board(board)
solve(board)
print('--------SOLVED------------\n')
print_board(board)