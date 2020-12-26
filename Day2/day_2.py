from collections import Counter

valid = []
# Part 1
with open('input.txt') as inp_file:
    for line in inp_file:
        pol, password = line.split(': ')
        comp, let = pol.split()
        gt, lt = list(map(int,comp.split('-')))
        freqs = Counter(password)

        if freqs[let] <= lt and freqs[let] >= gt:
            valid.append(password)

print(len(valid))

# Part 2
valid = []
with open('input.txt') as inp_file:
    for line in inp_file:
        pol, password = line.split(': ')
        comp, let = pol.split()
        pos1, pos2 = list(map(int,comp.split('-')))
        if (password[pos1-1] == let) != ((password[pos2-1] == let)):
            valid.append(password)

print(len(valid))