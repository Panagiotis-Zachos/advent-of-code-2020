f = open('input.txt').read()

group_answers = f.split('\n\n')

answer_part1 = 0

for group in group_answers:
    answer_part1 += len(set(group.replace('\n','')))

print(answer_part1)

answer_part2 = 0
for group in group_answers:
    people = group.split('\n')
    people = list(map(set, people))
    
    uniques = people[0]
    for i in range(1, len(people)):
        uniques = uniques.intersection(people[i])
    answer_part2 += len(uniques)

print(answer_part2)