instructions = []

with open("Day8Input.txt", "r") as f:
    for line in f:
        instructions.append(line.strip().split())

register_dict = {}

for item in instructions:
    register_dict[item[0]] = 0
    if item[1] == "dec":
        item[2] = -int(item[2])
    elif item[1] == "inc":
        item[2] = int(item[2])
    item[4] = 'register_dict["{0}"]'.format(item[4])

maximum = 0

for item in instructions:
    if eval(" ".join(item[4:])):
        register_dict[item[0]] += item[2]
        if register_dict[item[0]] > maximum:
            maximum = register_dict[item[0]]

print(maximum)

# Round 1
# maximum = 0
#
# for item in register_dict.keys():
#     if register_dict[item] > maximum:
#         maximum = register_dict[item]
#
# print(maximum)
