file1 = open('Day3/input.txt', 'r')
# file1 = open('Day3/example.txt', 'r')
Lines = file1.readlines()

gamma_rate = ""
epsilon_rate = ""

for i in range(12):
    print(i)
    
    count_zero = 0
    count_one = 0

    for line in Lines:
        digit = line[i:i+1]
        if digit == '1':
            count_one  += 1
        if  digit == '0':
            count_zero += 1
            
    if count_one > count_zero:
        gamma_rate += '1'
    else:
        gamma_rate += '0'

epsilon_rate = ''.join('1' if x == '0' else '0' for x in gamma_rate)

print(int(gamma_rate,2) * int(epsilon_rate,2))

