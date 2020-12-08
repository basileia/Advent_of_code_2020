with open("input.txt", encoding="utf-8") as file:
    instructions = file.read().split("\n")

for i in range(len(instructions)):
    instructions[i] = instructions[i].split()


accumulator = 0
i = 0
used_instructions = []

while i not in used_instructions:
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

print(accumulator)
