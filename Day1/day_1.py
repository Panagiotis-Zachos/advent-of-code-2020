
numbers = []

with open('input.txt') as inp_file:
    for line in inp_file:
        numbers.append(int(line.strip()))

numbers.sort(reverse=True)

# Part 1
for i in range(len(numbers)):
    for j in range(len(numbers)-1,i+1,-1):
        if numbers[i] + numbers[j] > 2020:
            break
        elif numbers[i] + numbers[j] == 2020:
            print(numbers[i]*numbers[j])

# Part 2
for i in range(len(numbers)):
    for j in range(len(numbers)-1,i+1,-1):
        if numbers[i] + numbers[j] >= 2020:
            break
        else:
            for k in range(j-1,i+1,-1):
                if numbers[i] + numbers[j] + numbers[k] > 2020:
                    break
                elif numbers[i] + numbers[j] + numbers[k] == 2020:
                    print(numbers[i] * numbers[j] * numbers[k])