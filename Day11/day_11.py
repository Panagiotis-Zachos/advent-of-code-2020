from time import time

def print_near(seats,i): # For debugging
    print(seats[i-1])
    print(seats[i])
    print(seats[i+1])

def pad_seats(array):
    seats = array.copy()
    X = len(seats) + 3
    
    # Pad Lines
    for i in range(len(seats)):    
        seats[i] = '.{}.'.format(seats[i])
    
    # Pad Columns
    X_pad = ''.join(['.'] * X)
    seats.append(X_pad)
    seats.insert(0, X_pad)
    return seats

# Part 1 functions
def count_adj_occ(seats, x, y):
    occupied = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i == j == 0: continue
            if seats[x+i][y+j] == '#': occupied += 1
    return occupied

def rule1(seats):
    temp_seats = seats.copy()
    for i in range(1, len(seats)-1):
        for j in range(1, len(seats[i])-1):
            if seats[i][j] == 'L' and count_adj_occ(seats,i,j) == 0:
                temp_seats[i] = temp_seats[i][0:j] + '#' + temp_seats[i][j+1:]
    return temp_seats

def rule2(seats):
    temp_seats = seats.copy()
    for i in range(1, len(seats)-1):
        for j in range(1, len(seats[i])-1):
            if seats[i][j] == '#' and count_adj_occ(seats,i,j) >= 4:
                temp_seats[i] = temp_seats[i][0:j] + 'L' + temp_seats[i][j+1:]

    return temp_seats

def solve_Part1():
    seats = open('input.txt').read().split('\n')
    seats = pad_seats(seats)

    prev_seats = []
    while prev_seats != seats:
        prev_seats = seats.copy()
        seats = rule2(rule1(seats))
    
    count_part1 = 0
    for line in seats:
        count_part1 += line.count('#')
    print(count_part1)


# Part 2 functions
def diag_helper(seats, x, y, dir_i, dir_j):
    i = dir_i
    j = dir_j
    while 0 <= x + i < len(seats)  and 0 <= y + j < len(seats[0]):
        # print(x+i, y+j, dir_i, dir_j, len(seats))
        if seats[x + i][y + j] == 'L': return 0
        elif seats[x + i][y + j] == '#': return 1
        i += dir_i
        j += dir_j
    return 0

def count_seen_occ(seats,x,y):
    occupied = 0

    for i_dir in range(-1,2):
        for j_dir in range(-1,2):
            if i_dir == j_dir == 0: continue
            occupied += diag_helper(seats, x, y, i_dir, j_dir)

    return occupied

def rule1_p2(seats):
    temp_seats = seats.copy()
    for i in range(1, len(seats)-1):
        for j in range(1, len(seats[i])-1):
            if seats[i][j] == 'L' and count_seen_occ(seats,i,j) == 0:
                temp_seats[i] = temp_seats[i][0:j] + '#' + temp_seats[i][j+1:]
    return temp_seats

def rule2_p2(seats):
    temp_seats = seats.copy()
    for i in range(1, len(seats)-1):
        for j in range(1, len(seats[i])-1):
            if seats[i][j] == '#' and count_seen_occ(seats,i,j) >= 5:
                temp_seats[i] = temp_seats[i][0:j] + 'L' + temp_seats[i][j+1:]

    return temp_seats

def solve_Part2():
    seats = open('input.txt').read().split('\n')
    seats = pad_seats(seats)

    prev_seats = []
    while prev_seats != seats:
        prev_seats = seats.copy()
        seats = rule2_p2(rule1_p2(seats))
    
    count_part2 = 0
    for line in seats:
        count_part2 += line.count('#')
    print(count_part2)

if __name__ == '__main__':
    t0 = time()
    solve_Part1()
    print(time() - t0)

    t0 = time()
    solve_Part2()
    print(time() - t0)