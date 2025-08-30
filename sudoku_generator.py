from random import*


def print_board(b):
    for i in range(len(b)):
        print(b[i], end="")
        if i % 3 == 0 and i != 0:
            print(' | ',end="")
        if i % 8 == 0:
            print(' ')

def fill():
    b = []
    for x in range(9):
        for y in range(9):
            b.append(0)
    return b

def distinct (b, number, row, col):

    test = True
    # check in row
    for i in range(len(b)):
        if number == b[row][i]:
            test = False

    # check in col
    for j in range(len(b)):
        if number == b[j][col]:
            test = False

    # check in grid
    init, stop = (0, 3) if row // 3 == 0 else (3, 6) if row // 3 == 1 else (6, 9)
    init2, stop2 = (0, 3) if col // 3 == 0 else (3, 6) if col // 3 == 1 else (6, 9)

    for i in range(init, stop):
        for j in range(init2, stop2):
            if number == b[i][j]:
                test = False

    return test

def generate(b):

    for g in range(25):   # 24 clues needed
        row = randint(0,8)
        col = randint(0,8)
        rand = randint(1,9)
        if(distinct(b,rand,row,col)):
            b[row][col] = rand
        else:
            b[row][col] = 0
    return b


# main prog

B = fill()
print_board(B)
print(generate(B))
print_board(B)