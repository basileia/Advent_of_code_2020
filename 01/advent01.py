def load_file():
    with open("expense_report_input.txt", encoding="utf-8") as file:
        all_lines = [int(line.strip()) for line in file.readlines()]
    return all_lines


def search_sum_to_2020(new_lines):
    for i in range(len(new_lines)):
        for j in range(len(new_lines) - 1):
            for k in range(len(new_lines) - 2):
                if 2020 - int(new_lines[i]) - int(new_lines[j]) - int(new_lines[k]) == 0:
                    return int(new_lines[i]), int(new_lines[j]), int(new_lines[k])
    return None


def multiply_numbers(numbers):
    number1, number2, number3 = numbers
    return number1 * number2 * number3


lines = load_file()
numbers = search_sum_to_2020(lines)
print(multiply_numbers(numbers))
