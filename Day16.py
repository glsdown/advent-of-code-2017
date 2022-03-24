def spin(my_list, x):
    my_list[:] = my_list[len(my_list) - x :] + my_list[: len(my_list) - x]


def exchange(my_list, x, y):
    my_list[x], my_list[y] = my_list[y], my_list[x]


def partner(my_list, a, b):
    pos_a = my_list.index(a)
    pos_b = my_list.index(b)
    my_list[pos_a] = b
    my_list[pos_b] = a


original_string = "abcdefghijklmnop"

with open("Day16Input.txt", "r") as f:
    dance_list = f.read().lower().split(",")

# TEST DATA
# dance_list = ["s1", "x3/4", "pe/b"]
# original_string = "abcde"

position_list = list(original_string)
moves = []

for item in dance_list:
    if item[0] == "s":
        # ROUND 2
        moves.append("spin(position_list, " + "".join(item[1:]) + ")")
        # ROUND 1
        # spin(position_list, int(''.join(item[1:])))
    elif item[0] == "x":
        values = item[1:].split("/")
        # ROUND 2
        moves.append("exchange(position_list, " + values[0] + "," + values[1] + ")")
        # ROUND 1
        # exchange(position_list, int(values[0]) , int(values[1]))
    elif item[0] == "p":
        values = item[1:].split("/")
        # ROUND 2
        moves.append('partner(position_list, "' + values[0] + '","' + values[1] + '")')
        # ROUND 1
        # partner(position_list, values[0], values[1])


# ROUND 2 ONLY FROM HERE


def get_move_functions():
    while True:
        yield (eval("lambda: " + move) for move in moves)


move_functions = get_move_functions()

# Find where repetition occurs
count = 1
while True:
    for move in next(move_functions):
        move()
    if "".join(position_list) == original_string:
        print("Repeats every", count)
        break
    count += 1

print("Calculating the final string...")
# After 60 loops, the string goes back to the original.
for i in range(1000000000 % count):
    for move in next(move_functions):
        move()

print("".join(position_list))
