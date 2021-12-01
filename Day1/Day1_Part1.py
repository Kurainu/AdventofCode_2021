file1 = open('Day1/input.txt', 'r')
Lines = file1.readlines()

Counter = 0
linebefore = 0

for line in Lines:
    print(line)
    print(linebefore)
    if int(line) > int(linebefore):
        Counter += 1
    linebefore = line

print(Counter-1)
