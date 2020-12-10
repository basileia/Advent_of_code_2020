with open("input.txt", encoding="utf-8") as file:
    instructions = file.read().split("\n")

for i in range(len(instructions)):
    instructions[i] = instructions[i].split()


def is_infinite(instructions):
    accumulator = 0
    i = 0
    used_instructions = []
    while i not in used_instructions:
        if i >= len(instructions) - 1:
            return False, accumulator
        if instructions[i][0] == "nop":
            used_instructions.append(i)
            i += 1
        elif instructions[i][0] == "acc":
            accumulator += int(instructions[i][1])
            used_instructions.append(i)
            i += 1
        elif instructions[i][0] == "jmp":
            used_instructions.append(i)
            i += int(instructions[i][1])
    return True, None


for j in range(len(instructions) - 1):
    if instructions[j][0] == "jmp":
        instructions[j][0] = "nop"
        result = is_infinite(instructions)
        if False in result:
            print(result)
            break
        instructions[j][0] = "jmp"
