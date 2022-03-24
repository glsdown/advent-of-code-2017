firewall = {}

with open("Day13Input.txt") as f:
    for line in f:
        current = line.strip().split(": ")
        firewall[int(current[0])] = 2 * int(current[1]) - 2

"""firewall = {0: 4,
            1: 2,
            4: 6,
            6: 6}"""

delay = 0
while True:

    hit = 0
    if any([((delay + key) % firewall[key] == 0) for key in list(firewall.keys())]):
        hit += 1

    if hit == 0:
        print("Through with", delay, "seconds delay!")
        break
    else:
        delay += 1
        if delay % 100000 == 0:
            print(delay)


"""ROUND 1


with open("Day13Input.txt") as f:
    for line in f:
        current = line.strip().split(": ")
        firewall[int(current[0])] = [int(current[1], 0, 1]

firewall = {0: [3, 0, 1],
            1: [2, 0, 1],
            4: [4, 0, 1],
            6: [4, 0, 1]}

hit = 0

for i in range(max(list(firewall.keys()))+1):
    try:
        if firewall[i][1] == 0:
            hit += i * firewall[i][0]
    except KeyError:
        pass
    for key in firewall.keys():
        firewall[key][1] += firewall[key][2]
        if firewall[key][1] % (firewall[key][0]-1) == 0:
            firewall[key][2] *= -1
 """


"""OLD CODE
for j in range(delay):
    for key in firewall.keys():
        firewall[key][1] += firewall[key][2]
        if firewall[key][1] % (firewall[key][0] - 1) == 0:
            firewall[key][2] *= -1
            
            
            
    for i in range(max(list(firewall.keys()))+1):
        try:
            if firewall[i][1] == 0:
                hit += 1
        except KeyError:
            pass
        for key in firewall.keys():
            firewall[key][1] = (firewall[key][1] + 1) % firewall[key][0]"""

"""for key in firewall.keys():
    length = firewall[key]
    firewall[key][1] = delay % length"""
