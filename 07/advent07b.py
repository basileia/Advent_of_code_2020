with open("input.txt", encoding="utf-8") as file:
    rules = file.readlines()

result = {}
for item in rules:
    key, val = item.strip().replace(".", "").split(" contain ", 1)
    result[key] = val.split(", ")


def get_sum(curr_bag):
    sum = 0
    children = []
    for bag in result:
        if curr_bag == bag:
            children = [item for item in result[bag]]
    for child in children:
        if child == "no other bags":
            continue
        if child:
            if child[2:][-1] != "s":
                child = child + "s"
            sum += int(child[0]) + int(child[0]) * get_sum(child[2:])
    return sum


print(get_sum("shiny gold bags"))
