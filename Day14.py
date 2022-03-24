import random

seed = "ugkiagan"
# seed = "flqrgnkx"

# Round 1
hex_values = {
    "0": 0,  # 0000
    "1": 1,  # 0001
    "2": 1,  # 0010
    "3": 2,  # 0011
    "4": 1,  # 0100
    "5": 2,  # 0101
    "6": 2,  # 0110
    "7": 3,  # 0111
    "8": 1,  # 1000
    "9": 2,  # 1001
    "a": 2,  # 1010
    "b": 3,  # 1011
    "c": 2,  # 1100
    "d": 3,  # 1101
    "e": 3,  # 1110
    "f": 4,  # 1111
}

# ROUND 2
hex_values = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111",
}


def knot_hash(string):
    current = 0
    skip_size = 0
    numbers = [i for i in range(256)]

    lengths = [ord(i) for i in string] + [17, 31, 73, 47, 23]

    for _ in range(64):
        for length in lengths:
            # reverse order of elements
            list_to_reverse = numbers[current:] + numbers[:current]
            list_to_reverse = list_to_reverse[length - 1 :: -1]

            for counter in range(length):
                new_current = (current + counter) % len(numbers)
                numbers[new_current] = list_to_reverse[counter]

            current = (current + length + skip_size) % len(numbers)
            skip_size += 1

    dense_hash = []
    row = 0
    counter = 0
    # numbers = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
    for number in numbers:
        row ^= number
        counter += 1
        if counter % 16 == 0:
            dense_hash.append(row)
            row = 0

    hex_string = [str(hex(i))[2:] for i in dense_hash]
    hash = ""
    for item in hex_string:
        if len(item) == 1:
            hash += "0" + item
        else:
            hash += item
    return hash


knot_hash_result = []

for i in range(128):
    knot_hash_result.append(knot_hash(seed + "-" + str(i)))
print(knot_hash_result)

grid = []
# Round 1
# used = 0

for row in knot_hash_result:
    # round 2 only
    used = ""
    for letter in row:
        used += hex_values[letter]
    # round 2 only
    grid.append(used)

print(grid)


def check_neighbour(row, column):

    if row < 0 or column < 0:
        return False
    try:
        return grid[row][column] == "1"
    except IndexError:
        return False


total = 0

with open("Day14Input.txt", "w") as f:

    for row in range(128):
        for column in range(128):
            if grid[row][column] == "1":
                text_to_write = "[" + str(row) + "," + str(column) + "] <-> "

                new_row = row + 1
                new_column = column
                if check_neighbour(new_row, new_column):
                    text_to_write += "[" + str(new_row) + "," + str(new_column) + "]+"

                new_row = row - 1
                new_column = column
                if check_neighbour(new_row, new_column):
                    text_to_write += "[" + str(new_row) + "," + str(new_column) + "]+"

                new_row = row
                new_column = column + 1
                if check_neighbour(new_row, new_column):
                    text_to_write += "[" + str(new_row) + "," + str(new_column) + "]+"

                new_row = row
                new_column = column - 1
                if check_neighbour(new_row, new_column):
                    text_to_write += "[" + str(new_row) + "," + str(new_column) + "]+"

                if text_to_write == "[" + str(row) + "," + str(column) + "] <-> ":
                    total += 1
                else:
                    f.write(text_to_write[:-1] + "\n")

memory_dict = {}

with open("Day14Input.txt", "r") as f:
    for line in f:
        current = line.split(" <-> ")
        memory_dict[current[0]] = [i.strip() for i in current[1].strip().split("+")]

print(memory_dict)


def recursive_dfs(graph, start, path=[]):
    """recursive depth first search from start"""
    path = path + [start]
    for node in graph[start]:
        if not node in path:
            path = recursive_dfs(graph, node, path)
    return path


while True:
    current = random.choice(list(memory_dict.keys()))
    group = recursive_dfs(memory_dict, current)
    total += 1
    for item in group:
        del memory_dict[item]
    if len(memory_dict.keys()) == 0:
        break

print(total)
