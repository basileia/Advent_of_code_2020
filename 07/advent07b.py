import re

with open("sample.txt", encoding="utf-8") as file:
    rules = file.readlines()

result = {}
for item in rules:
    key, val = item.strip().replace(".", "").split(" contain", 1)
    result[key] = val.split(", ")


values_bags = []


def get_sum(search_value, number_of_bags, sum):
    wanted = result[search_value]
    for i in wanted:
        try:
            num = int(re.match(r"\d", i.strip()).group())
            values_bags.append(i)
            sum += number_of_bags * num
        except AttributeError:
            values_bags.append(i)
    return sum


values_bags.append("shiny gold bags")
sum = get_sum("shiny gold bags", 1, 0)
num = 1

for values_bag in values_bags:
    value = re.search(r"([a-z]+([a-z]| ))+", values_bag.lstrip()).group()
    if value[-1] != "s":
        value = value + "s"
    if value == "no other bags":
        continue
    if value == "shiny gold bags":
        continue
    num = int(re.match(r"\d", values_bag.lstrip()).group()) * num
    sum = get_sum(value, num, sum)
print(sum)
