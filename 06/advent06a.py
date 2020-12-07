with open("input.txt", encoding="utf-8") as file:
    answers = file.read().split("\n\n")

sum = 0
for answer in answers:
    unique_answers = set("".join(answer.split()))
    sum += len(unique_answers)

print(sum)
