# Part 1
total_trees = 0
pos = 3
flag = True
with open('input.txt') as inp_file:
    for line in inp_file:
        if flag:
            flag = False
            continue
        if line[pos] == '#':
            total_trees += 1
        pos = (pos + 3) % len(line.strip())

print(total_trees)

# Part 2

def find_trees(slope, tree_map):
    right, down = slope
    total_trees = 0
    pos = right
    # print(right,d)
    for i in range(down,323,down):
        if tree_map[i][pos] == '#':
            total_trees += 1
        pos = (pos + right) % 31
    return total_trees

tree_map = open('input.txt').read().split('\n')
# print(tree_map[0])
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

prod = 1
for slope in slopes:
    prod *= find_trees(slope, tree_map)
print(prod)