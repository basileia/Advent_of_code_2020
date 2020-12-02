with open("input.txt", encoding="utf-8") as file:
    valid_passwords = 0

    for line in file:
        position = 0
        positions, password = line.split(":")
        min, max_letter = positions.split("-")
        max, letter = max_letter.split(" ")
        password = password.strip()
        if password[int(min) - 1] == letter:
            position += 1
        if password[int(max) - 1] == letter:
            position += 1
        if position == 1:
            valid_passwords += 1

print(valid_passwords)
