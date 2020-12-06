import re

with open("input.txt", encoding="utf-8") as file:
    lines = file.read()
    passports = re.split(r"\n\n", lines)

valid_parts = 0
valid = 0
count = 0
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
reg_rules = []

reg_rules.append(re.compile(r"byr:(19[2-9]\d)|(200[0-2])"))
reg_rules.append(re.compile(r"iyr:20(1\d|20)"))
reg_rules.append(re.compile(r"eyr:20(2\d|30)"))
reg_rules.append(re.compile(r"hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)"))
reg_rules.append(re.compile(r"hcl:#([0-9a-f]){6}"))
reg_rules.append(re.compile(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)"))
reg_rules.append(re.compile(r"pid:(\d){9}"))

for i in range(len(passports)):
    for req in required:
        if req in passports[i]:
            count += 1
    if count == len(required):
        for regex in reg_rules:
            if regex.search(passports[i]):
                valid_parts += 1
        if valid_parts == len(required):
            valid += 1
        valid_parts = 0
    count = 0

print(valid)
