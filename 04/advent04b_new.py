import re


with open("input.txt", encoding="utf-8") as file:
    passports = file.read().split("\n\n")

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

data = []
for record in passports:
    record_dict = {}
    for item in record.split():
        record_dict[item[:3]] = item[4:]
    data.append(record_dict)


def valid_requirements(data):
    count = 0
    valid_requirements = []
    for r_dict in data:
        for req in required:
            if req in r_dict.keys():
                count += 1
        if count == len(required):
            valid_requirements.append(r_dict)
        count = 0
    return valid_requirements


def valid_passport(selected_passport):
    if not 1920 <= int(selected_passport["byr"]) <= 2002:
        return False
    if not 2010 <= int(selected_passport["iyr"]) <= 2020:
        return False
    if not 2020 <= int(selected_passport["eyr"]) <= 2030:
        return False
    if selected_passport["hgt"]:
        if "cm" in selected_passport["hgt"]:
            if not 150 <= int(''.join(i for i in selected_passport["hgt"] if i.isdigit())) <= 193:
                return False
        elif "in" in selected_passport["hgt"]:
            if not 59 <= int(''.join(i for i in selected_passport["hgt"] if i.isdigit())) <= 76:
                return False
        else:
            return False
    if not re.match(r"#([0-9a-f]){6}", selected_passport["hcl"]):
        return False
    if not re.match(r"amb|blu|brn|gry|grn|hzl|oth", selected_passport["ecl"]):
        return False
    if not (len(selected_passport["pid"]) == 9 and selected_passport["pid"].isdigit()):
        return False
    return True


valid = 0
for_validation = valid_requirements(data)
for passport in for_validation:
    if valid_passport(passport):
        valid += 1
print(valid)
