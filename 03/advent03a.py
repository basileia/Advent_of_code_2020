with open("input.txt", encoding="utf-8") as file:
    all_lines = [line.strip() for line in file]

trees = 0
col = 0
for row in range(len(all_lines)):
    if row != 0:
        col += 3
        if all_lines[row][col % len(all_lines[0])] == "#":
            trees += 1

print(trees)
