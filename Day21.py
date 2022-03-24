import numpy as np

# Get the rules from the text file
rules = {}

with open("Day21Input.txt", "r") as file:
    for line in file:
        name, property = line.strip().split(" => ")
        rules[name] = property

# Create 'flipped' rules
# FV, FH, R90, R180, R270 and combining them
def flip_vert(shape):
    return "/".join(shape.split("/")[::-1])


def flip_hor(shape):
    return "/".join([row[::-1] for row in shape.split("/")])


def rot90(shape):
    shape = shape.split("/")
    return "/".join(["".join(row) for row in list(zip(*shape[::-1]))])


def rot180(shape):
    return rot90(rot90(shape))


def rot270(shape):
    return rot90(rot180(shape))


original_keys = [i for i in rules.keys()]

for key in original_keys:
    value = rules[key]
    rules[flip_vert(key)] = value
    rules[flip_hor(key)] = value

    rot = [rot90(key), rot180(key), rot270(key)]
    for val in rot:
        rules[flip_vert(val)] = value
        rules[flip_hor(val)] = value
        rules[val] = value

print(rules)

grid = ".#./..#/###"


def string_to_array(my_string):
    return np.array([list(i) for i in my_string.split("/")])


def array_to_string(my_array):
    return "/".join(["".join(item) for item in my_array])


grid = string_to_array(grid)

# Carry out growth iterations
for i in range(18):
    print("Round:", i)
    if len(grid) % 2 == 0:
        jump = 2
    elif len(grid) % 3 == 0:
        jump = 3
    rows = []
    for row in range(0, len(grid), jump):
        column_matrices = []
        for column in range(0, len(grid), jump):
            my_grid = grid[row : row + jump, column : column + jump]
            column_matrices.append(string_to_array(rules[array_to_string(my_grid)]))
        rows.append(np.concatenate(column_matrices, axis=1))
    grid = np.concatenate(rows)

# Print how many are a hash
print(sum(x == "#" for x in array_to_string(grid)))
