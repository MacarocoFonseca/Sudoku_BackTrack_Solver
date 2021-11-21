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

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

print_board(board)

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])): # len of each 0
            if bo[i][j] == 0:
                return(i, j) # row, col
    return None


def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])): # always 9..
        if bo[pos[0]][i] == num and pos[1] != i: # check if I just inserted a number into then I won't bother with that
            return False    

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i: # loops downd over the row
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # loop inside the box and check if the number does not appear twice.
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos: # check if the any number is dif. from the one I just added 
                return False

    return True

def solve(bo):
    print(bo)
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row,col)):     # check if adding nr 1-9 is a valid solution
            bo[row][col] = i            # add one number

            if solve(bo):
                return True
            
            bo[row][col] = 0

print_board(board)
print("__________________________")
solve(board)
print("__________________________")
print_board(board)