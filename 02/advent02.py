with open("input.txt", encoding="utf-8") as file:
    valid_passwords = 0

    for line in file:
        limits, password = line.split(":")
        min, max_letter = limits.split("-")
        max, letter = max_letter.split(" ")
        if password.count(letter) >= int(min) and password.count(letter) <= int(max):
            valid_passwords += 1

print(valid_passwords)
