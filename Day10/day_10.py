adapters = list(map(int, open('input.txt').read().split('\n')))

adapters.sort()
# Part 1
dif1 = 1
dif3 = 1
for i in range(1, len(adapters)):
    dif = adapters[i] - adapters[i-1]
    if dif == 1: dif1 += 1
    elif dif == 3: dif3 += 1

print(dif3*dif1)

# Part 2.1
adapters.append(adapters[-1] + 3)
adapters.insert(0, 0)

paths = [0 for i in range(len(adapters))]
paths[0] = 1

for i in range(1, len(adapters)):
    paths[i] = paths[i - 1]
    if i > 1 and adapters[i] - adapters[i - 2] <= 3:
        paths[i] += paths[i - 2]
    if i > 2 and adapters[i] - adapters[ i - 3] <= 3:
        paths[i] += paths[i - 3]

print(paths[-1])

# Part 2.2
curr = 0
p1 = 1
p2 = 0
p3 = 0

for i in range(1, len(adapters)):
    curr = p1
    if i > 1 and adapters[i] - adapters[i - 2] <= 3:
        curr += p2
    if i > 2 and adapters[i] - adapters[ i - 3] <= 3:
        curr += p3
    p3, p2, p1 = (p2, p1, curr)

print(curr)
