
def bin_sectors(low, high, letters):
    # F, L means take the lower half, reduce the high lim
    # B, R means take the upper half, reduce the low lim
    
    for let in letters:
        red = round((high - low) / 2 + 0.001)
        if let in 'FL': high = high - red
        elif let in 'BR': low = low + red
    return low

def seatID_calc(boarding_pass):
    return bin_sectors(0,127,boarding_pass[:7]) * 8 + bin_sectors(0,7,boarding_pass[7:])

f = open('input.txt')

seat_IDs = []
for line in f:
    seat_IDs.append(seatID_calc(line))

# print(max(seat_IDs))

seat_IDs.sort()


for i in range(2,len(seat_IDs)):
    # print(i)
    if seat_IDs[i] != seat_IDs[i-1] + 1:
        print(seat_IDs[i]-1)