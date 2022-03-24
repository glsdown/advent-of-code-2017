import numpy as np

with open("Day22Input.txt", "r") as file:
    nodes = np.array(
        [
            ["." for i in range(2000)] + list(line) + ["." for j in range(2000)]
            for line in file.read().split("\n")
        ]
    )


width = len(nodes[0])

nodes = np.concatenate(
    (
        [["." for i in range(width)] for j in range(2000)],
        nodes,
        [["." for i in range(width)] for j in range(2000)],
    )
)

print(nodes)

# row, column
current = [len(nodes) // 2, len(nodes[0]) // 2]
direction = [-1, 0]
right = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
left = {(-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0)}

counter = 0
for i in range(10000000):
    if i % 100000 == 0:
        print("Round:", i, i * 100 // 10000000, "% through")

    # If it is clean it turns left and weakens it
    if nodes[current[0]][current[1]] == ".":
        nodes[current[0]][current[1]] = "W"
        direction = list(left[tuple(direction)])
    # If it is weakened, infect it.
    elif nodes[current[0]][current[1]] == "W":
        nodes[current[0]][current[1]] = "#"
        counter += 1
    # If currently infected...
    elif nodes[current[0]][current[1]] == "#":
        nodes[current[0]][current[1]] = "F"
        direction = list(right[tuple(direction)])
    # If currently flagged, reverses direction
    elif nodes[current[0]][current[1]] == "F":
        nodes[current[0]][current[1]] = "."
        direction = [-i for i in direction]

    current[0] += direction[0]
    current[1] += direction[1]

print(counter)


# ROUND 1
"""
counter = 0
for i in range(10000):
    if i % 1000 == 0:
        print("Round:", i)

    # If currently infected, turn right
    if nodes[current[0]][current[1]] == "#":
        nodes[current[0]][current[1]] = "."
        direction = list(right[tuple(direction)])
    else:
        nodes[current[0]][current[1]] = "#"
        counter += 1
        direction = list(left[tuple(direction)])

    current[0] += direction[0]
    current[1] += direction[1]

print(counter)"""
