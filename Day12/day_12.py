from math import cos, sin, radians

def solve1():
    instructions = open('input.txt').read().split('\n')

    DIRECTIONS = 'NESW'
    FACING_INDEX = 1

    # Let Ship start at (0,0) positive movement is N,E negative is S,W 
    POS_X = 0
    POS_Y = 0
    
    for inst in instructions:
        comm, val = (inst[:1], int(inst[1:]))

        if comm == 'F': comm = DIRECTIONS[FACING_INDEX]
        
        if comm == 'L': FACING_INDEX = (FACING_INDEX - int(val / 90)) % 4
        elif comm == 'R': FACING_INDEX = (FACING_INDEX + int(val / 90)) % 4
        elif comm == 'N': POS_Y += val
        elif comm == 'E': POS_X += val
        elif comm == 'S': POS_Y -= val
        elif comm == 'W': POS_X -= val

    print(abs(POS_X) + abs(POS_Y))

# Part 2
def rotate(point, theta):
    theta = radians(theta)
    px, py = point

    qx = round(cos(theta) * px - sin(theta) * py)
    qy = round(sin(theta) * px + cos(theta) * py)
    return qx, qy

def solve2():
    instructions = open('input.txt').read().split('\n')

    # Let Ship start at (0,0) positive movement is N,E negative is S,W 
    SHIP_X = 0
    SHIP_Y = 0

    WAY_X = 10
    WAY_Y = 1

    for inst in instructions:
        comm, val = (inst[:1], int(inst[1:]))
        
        # print(inst, end=' ')
        if comm == 'L': WAY_X, WAY_Y = rotate((WAY_X,WAY_Y), val)
        elif comm == 'R': WAY_X, WAY_Y = rotate((WAY_X,WAY_Y), -val)
        elif comm == 'N': WAY_Y += val
        elif comm == 'E': WAY_X += val
        elif comm == 'S': WAY_Y -= val
        elif comm == 'W': WAY_X -= val
        elif comm == 'F':
            SHIP_X += val * WAY_X 
            SHIP_Y += val * WAY_Y
    print(abs(SHIP_X) + abs(SHIP_Y))

if __name__ == '__main__':
    solve1()
    solve2()
