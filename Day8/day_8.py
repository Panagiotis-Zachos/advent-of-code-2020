from time import time

def execute_code(instructions):
    visits = [0 for i in range(len(instructions))]
    accumulator = 0
    point = 0
    visits[0] = 1
    while True:
        c_inst, val = instructions[point].split()
        val = int(val)
        if c_inst == 'acc': 
            accumulator += val
        elif c_inst == 'nop': 
            pass
        elif c_inst == 'jmp':
            point += val - 1
        if point >= len(instructions) - 1:
            return True, accumulator
        point += 1
        if visits[point] == 1:
            return False, accumulator
        visits[point] = 1

# Part 1
def part1():
    instructions = open('input.txt').read().split('\n')
    
    _, acc = execute_code(instructions)
    print(acc)


# Part 2
# This is a terrible solution but I couldn't be bothered to write another DFS
def part2():
    instructions = open('input.txt').read().split('\n')

    for i in range(len(instructions)):
        if 'acc' in instructions[i]:
            continue

        elif 'jmp' in instructions[i]: 
            instructions[i] = instructions[i].replace('jmp','nop')
            flag, acc = execute_code(instructions)
            instructions[i] = instructions[i].replace('nop','jmp')
            if flag:
                print(acc)
                break

        elif 'nop' in instructions[i]: 
            instructions[i] = instructions[i].replace('nop','jmp')
            flag, acc = execute_code(instructions)
            instructions[i] = instructions[i].replace('jmp','nop')
            if flag:
                print(acc)
                break
        


if __name__ == '__main__':
    t0 = time()
    part1()
    print('Time for Part 1: {}',time()-t0)
    t0 = time()
    part2()
    print('Time for Part 2: {}',time()-t0)
    