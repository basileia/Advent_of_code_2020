with open("input.txt", encoding="utf-8") as file:
    all_lines = [line.strip() for line in file]


def trees(step_col, step_row, all_lines):
    trees = 0
    col = 0

    for row in range(0, len(all_lines), step_row):
        if row != 0:
            col += step_col
            if all_lines[row][col % len(all_lines[0])] == "#":
                trees += 1
    return trees


number = trees(1, 1, all_lines) * trees(3, 1, all_lines)
number *= trees(5, 1, all_lines) * trees(7, 1, all_lines)
number *= trees(1, 2, all_lines)

print(number)
