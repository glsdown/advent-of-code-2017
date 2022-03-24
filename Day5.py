jumps = []

with open("Day5Input.txt", "r") as f:
    for line in f:
        jumps.append(int(line))

print(jumps)

# jumps = [0,3,0,1,-3]
jumps_made = 0
index = 0

# Round 1
"""try:
    while True:
        current = jumps[index]
        jumps[index] += 1
        index += current
        jumps_made += 1

except IndexError:
    print("Jumps Made:", jumps_made)"""

# Round 3
try:
    while True:
        current = jumps[index]
        if current >= 3:
            jumps[index] -= 1
        else:
            jumps[index] += 1
        index += current
        jumps_made += 1

except IndexError:
    print("Jumps Made:", jumps_made)
