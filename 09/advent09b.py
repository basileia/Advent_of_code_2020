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


def sum_invalid_number(data, number):
    numbers = []
    count = 0
    for i in range(len(data)):
        for j in range(count, i):
            numbers.append(data[j])
            total = sum(data[count:j+1])
            if total == number:
                return numbers
            elif total > number:
                numbers.clear()
                total = 0
                count += 1


invalid_number = invalid_number_in_row(xmas, 25)
wanted_numbers = sum_invalid_number(xmas, invalid_number)
print(min(wanted_numbers) + max(wanted_numbers))
