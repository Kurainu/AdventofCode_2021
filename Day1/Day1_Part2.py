file1 = open('Day1/input.txt', 'r')
Lines = file1.readlines()
Lines = list(map(int, Lines))

#Lines = [199,200,208,210,200,207,240,269,260,263]

count = 0
previous_sum = 0
for i in range(len(Lines)):
    measure_window = Lines[i:i+3]
    if len(measure_window) != 3:
        break

    if sum(measure_window) > previous_sum:
        count += 1
    previous_sum = sum(measure_window)

print(count - 1)