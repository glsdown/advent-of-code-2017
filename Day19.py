maze = []

with open("Day19Input.txt", "r") as f:
    for line in f:
        to_add = list(line)[:-1]
        maze.append(to_add + [" " for i in range(200 - len(to_add))])

# across then down!!
direction = [0, 1]
current = [1, 0]
been = []
steps = 0


def get_value(maze, current):
    try:
        return maze[current[1]][current[0]]
    except IndexError:
        return " "


while True:
    value = get_value(maze, current)
    print(current, 'is "' + value + '"')
    steps += 1
    if value == "|" and direction[1] != 0:
        current[1] += direction[1]
    elif value == "-" and direction[0] != 0:
        current[0] += direction[0]
    elif value == "+":
        if direction[0] != 0:
            # Moving across the board
            direction[0] = 0
            if get_value(maze, [current[0], current[1] + 1]) != " ":
                direction[1] = 1
                current[1] += direction[1]
            elif get_value(maze, [current[0], current[1] - 1]) != " ":
                direction[1] = -1
                current[1] += direction[1]
            else:
                print("Direction has failed...", direction)

        else:
            # Moving up/down the board
            direction[1] = 0
            if get_value(maze, [current[0] + 1, current[1]]) != " ":
                direction[0] = 1
                current[0] += direction[0]
            elif get_value(maze, [current[0] - 1, current[1]]) != " ":
                direction[0] = -1
                current[0] += direction[0]
            else:
                print("Direction has failed...", direction)
    elif value == " ":
        direction = [0, 0]
    else:
        if value not in "|-+ ":
            been.append(value)
        current = [x + y for x, y in zip(current, direction)]

    if direction == [0, 0]:
        steps -= 1
        break

print("".join(been))
print("Took", steps, "steps")
