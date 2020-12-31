from time import time

def check_validity(preamble, num_to_check):   
    for num in preamble:
        if num_to_check - num in preamble: return True
    return False


numbers = list(map(int,open('input.txt').read().split('\n')))

# Part 1
t0 = time()
for i in range(25, len(numbers)):
    preamble = numbers[i-25:i]
    num_to_check = numbers[i]

    if not check_validity(preamble, num_to_check): 
        print(num_to_check,i)
        break
print('Part 1 time: {}s'.format(time() - t0))

# Part 2
target = 375054920

flag = False
for i in range(len(numbers)-25):
    curr_sum = numbers[i]
    sum_list = [numbers[i]]
    j = i + 1
    while curr_sum < target:
        curr_sum += numbers[j]
        sum_list.append(numbers[j])
        if curr_sum == target:
            print(max(sum_list) + min(sum_list))
            flag = True
            break
        j += 1
    if flag: break