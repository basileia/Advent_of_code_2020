with open("input.txt", encoding="utf-8") as file:
    answers = file.read().split("\n\n")

sum = 0
for answer in answers:
    result = set(answer.split()[0]).intersection(*answer.split())
    sum += len(result)

print(sum)
