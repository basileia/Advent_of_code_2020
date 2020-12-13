with open("input.txt", encoding="utf-8") as file:
    xmas = [int(line.strip()) for line in file]


def invalid_number_in_row(data, preamble):
    count = 0
    for i in range(preamble, len(data)):
        target = data[i]
        valid = False
        for j in range(count, i):
            if data[j] < target:
                pair = target - data[j]
                if pair in data[count:i]:
                    if pair != data[j]:
                        valid = True
        count += 1
        if valid is False:
            return target


print(invalid_number_in_row(xmas, 25))
