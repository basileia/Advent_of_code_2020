with open("input.txt", encoding="utf-8") as file:
    adapters = [int(line.strip()) for line in file]

device = max(adapters) + 3

adapters.sort()


def diff(difference):
    if difference == 1:
        return 1
    elif difference == 2:
        return 2
    elif difference == 3:
        return 3


numbers = []
numbers.append(diff(adapters[0]))
for i in range(len(adapters) - 1):
    difference = adapters[i+1] - adapters[i]
    numbers.append(diff(difference))
numbers.append(diff(device - adapters[-1]))

print(numbers.count(1) * numbers.count(3))
