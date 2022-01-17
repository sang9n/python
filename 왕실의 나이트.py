import sys
sys.stdin = open("input.txt","rt")

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0]))-int(ord('a'))+1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    n_row = row + step[1]
    n_col = col + step[0]

    if n_row >= 1 and n_row <= 8 and n_col >= 1 and n_col <=8:
        result += 1

print(result)