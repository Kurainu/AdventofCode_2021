input = open('Day2/input.txt', 'r')
example = open('Day2/example.txt', 'r')
Lines = input.readlines()
#Lines = example.readlines()

horizontal_pos = 0
depth = 0
aim = 0

for line in Lines:
  direction, amount = line.split(' ')
  if direction == "forward":
    horizontal_pos += int(amount)
    depth += int(amount) * aim
  elif direction == "down":
    aim += int(amount)
  elif direction == "up":
    aim -= int(amount)

print(horizontal_pos)
print(depth)
print(horizontal_pos*depth)
