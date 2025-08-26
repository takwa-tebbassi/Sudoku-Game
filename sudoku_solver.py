Board = [
    [4, 0, 1, 2, 9, 0, 0, 7, 5],
    [2, 0, 0, 3, 0, 0, 8, 0, 0],
    [0, 7, 0, 0, 8, 0, 0, 0, 6],
    [0, 0, 0, 1, 0, 3, 0, 6, 2],
    [1, 0, 5, 0, 0, 0, 4, 0, 3],
    [7, 3, 0, 6, 0, 8, 0, 0, 0],
    [6, 0, 0, 0, 2, 0, 0, 3, 0],
    [0, 0, 7, 0, 0, 1, 0, 0, 4],
    [8, 9, 0, 0, 6, 5, 1, 0, 7],
]

def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("--------------------------------")

        for j in range(len(b[i])):
            if j % 3 == 0 and j != 0:
                print("|  ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(b[i][j], " ",end="")


def find_empty(b):
    lis = []
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i][j] == 0:
                lis.append([i, j])   # pos
    return lis


def find_potentials(b,pos):

    tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #  keep only unused ones

    # check in row
    for i in range(len(b)):
        if b[pos[0]][i] in tab:
            tab.remove(b[pos[0]][i]) 

    # check in col
    for j in range(len(b)):
        if b[j][pos[1]] in tab:
            tab.remove(b[j][pos[1]]) 

    # check in grid
    init, stop = (0, 3) if pos[0] // 3 == 0 else (2, 6) if pos[0] // 3 == 1 else (3, 9)
    init2, stop2 = (0, 3) if pos[1] // 3 == 0 else (2, 6) if pos[1] // 3 == 1 else (3, 9)

    for i in range(init, stop):
        for j in range(init2, stop2):
            if b[i][j] in tab:
                tab.remove(b[i][j]) 

    return tab

def distinct (b,number,pos):
    test = True
     # check in row
    for i in range(len(b)):
        if number == b[pos[0]][i]:
            test = False

    # check in col
    for j in range(len(b)):
        if number == b[j][pos[1]]:
            test = False

    # check in grid
    init, stop = (0, 3) if pos[0] // 3 == 0 else (2, 6) if pos[0] // 3 == 1 else (3, 9)
    init2, stop2 = (0, 3) if pos[1] // 3 == 0 else (2, 6) if pos[1] // 3 == 1 else (3, 9)

    for i in range(init, stop):
        for j in range(init2, stop2):
            if number == b[i][j]:
                test = False

    return test


def solve(b):
    
    position = find_empty(b)
    if len(position) == 0:
        return True
    
    for pos in position:
        tab = find_potentials(b,pos)
        for number in tab:
            check = distinct(b, number, pos)
            if(check):
                b[pos[0]][pos[1]] = number

                if solve(b):
                    return True
                
                b[pos[0]][pos[1]] = 0 # put it back to zero if it doesn't fit
                        
    return False


# main prog

print_board(Board)
if(solve(Board)):
    print('\nprocessing...')
    print('\nsolved board..\n')
    print_board(Board)