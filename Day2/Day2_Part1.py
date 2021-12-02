file1 = open('Day2/input.txt', 'r')
Lines = file1.readlines()

horizontal_pos = 0
depth = 0

for line in Lines:
  direction, amount = line.split(' ')
  if direction == "forward":
    horizontal_pos += int(amount)
  elif direction == "down":
    depth += int(amount)
  elif direction == "up":
    depth -= int(amount)

print(horizontal_pos*depth)
