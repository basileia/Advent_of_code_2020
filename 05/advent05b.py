with open("input.txt", encoding="utf-8") as file:
    board_passes = [line.strip() for line in file]


def get_row(board_pass, number, number_of_rows):
    board_row = board_pass[:number]
    interval = [0, number_of_rows - 1]

    for char in board_row:
        if char == "F":
            interval[1] -= number_of_rows / 2
            number_of_rows = number_of_rows / 2
        elif char == "B":
            interval[0] += number_of_rows / 2
            number_of_rows = number_of_rows / 2

    if interval[0] == interval[1]:
        return interval[0]
    else:
        return None


def get_column(board_pass, number, number_of_cols):
    board_col = board_pass[number:]
    interval = [0, number_of_cols - 1]

    for char in board_col:
        if char == "L":
            interval[1] -= number_of_cols / 2
            number_of_cols = number_of_cols / 2
        elif char == "R":
            interval[0] += number_of_cols / 2
            number_of_cols = number_of_cols / 2

    if interval[0] == interval[1]:
        return interval[0]
    else:
        return None


seat_ids = []
for board_pass in board_passes:
    id = get_row(board_pass, 7, 128) * 8 + get_column(board_pass, 7, 8)
    seat_ids.append(id)

missing = [x for x in range(int(min(seat_ids)), int(max(seat_ids))) if x not in seat_ids]
print(missing)
