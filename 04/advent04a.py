import re

with open("input.txt", encoding="utf-8") as file:
    lines = file.read()
    passports = re.split(r"\n\s*\n", lines)

valid = 0
count = 0
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for i in range(len(passports)):
    for req in required:
        if req in passports[i]:
            count += 1
    if count == len(required):
        valid += 1
    count = 0

print(valid)
