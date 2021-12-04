import re
import sys

file1 = open('Day4/example.input', 'r')
#file1 = open('Day4/stelar.input', 'r')
#file1 = open('Day4/input.input', 'r')
Lines = ''.join(file1.readlines()).split("\n\n")

num_Boards = len(Lines)
RNG_Numbers = Lines[0].split(",")


class Board:
    def __init__(self, board):
        self.data = board

    def Mark_Number(self, num):
        for i in range(0, 5):
            for j in range(0, 5):
                if self.data[i][j] != "marked" and int(self.data[i][j]) == int(num):
                    self.data[i][j] = "marked"

    def Bingo(self):
        for i in range(0, 5):
            if self.data[i][0] == "marked" and self.data[i][1] == "marked" and self.data[i][2] == "marked" and self.data[i][3] == "marked" and self.data[i][4] == "marked":
                return True
            if self.data[0][i] == "marked" and self.data[1][i] == "marked" and self.data[2][i] == "marked" and self.data[3][i] == "marked" and self.data[4][i] == "marked":
                return True

        return False

    def Get_Sum(self):
        sum = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if self.data[i][j] != "marked":
                    sum += int(board.data[i][j])
        return sum


Boards = []

# Populate Boards Array
for i in range(1, num_Boards):
    temp = []
    for row in Lines[i].split("\n"):
        temp.append(list(re.findall("(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", row)[0]))
    Boards.append(Board(temp))

# Draw the RNG Numbers
for num in RNG_Numbers:
    for board in Boards:
        board.Mark_Number(num)
    if board.Bingo() == True:
        found_bingo = True
        print("BINGOOOOOO")
        print(board.data)
        print(board.Get_Sum() * int(num))
        sys.exit(0)
