with open("input.txt", encoding="utf-8") as file:
    rules = file.readlines()

result = {}
for item in rules:
    key, val = item.strip().replace(".", "").split("contain", 1)
    result[key] = val.split(", ")


keys = []


def get_keys(search_value):
    for value in result.values():
        for i in range(len(value)):
            if search_value in value[i]:
                for key in result:
                    if value[i] in result[key]:
                        keys.append(key)
    return keys


get_keys("shiny gold bag")
for key in keys:
    get_keys(key[:-2])
print(len(set(keys)))
