with open("Day11Input.txt", "r") as f:
    directions = f.read().split(",")

# directions = "se,sw,se,sw,sw".split(",")
direction_dict = {"n": 0, "ne": 0, "se": 0, "s": 0, "sw": 0, "nw": 0}

# Round 1
for item in directions:
    direction_dict[item] += 1

print(direction_dict)

# Cancel out the NE and NW to N
direction_dict["n"] += min(direction_dict["ne"], direction_dict["nw"])
if direction_dict["ne"] > direction_dict["nw"]:
    direction_dict["ne"] = abs(direction_dict["ne"] - direction_dict["nw"])
    direction_dict["nw"] = 0
else:
    direction_dict["nw"] = abs(direction_dict["ne"] - direction_dict["nw"])
    direction_dict["ne"] = 0

# Cancel out the SE and SW to S
direction_dict["s"] += min(direction_dict["se"], direction_dict["sw"])
if direction_dict["se"] > direction_dict["sw"]:
    direction_dict["se"] = abs(direction_dict["se"] - direction_dict["sw"])
    direction_dict["sw"] = 0
else:
    direction_dict["sw"] = abs(direction_dict["se"] - direction_dict["sw"])
    direction_dict["se"] = 0

# Cancel out the SE and N to NE
direction_dict["ne"] += direction_dict["se"]
direction_dict["n"] = direction_dict["n"] - direction_dict["se"]
direction_dict["se"] = 0

# Cancel out the N and S
direction_dict["n"] -= direction_dict["s"]
direction_dict["s"] = 0

print(direction_dict["n"] + direction_dict["ne"])

# Round 2

current = [0, 0]
maximum = 0
for direction in directions:
    if direction == "n":
        current[1] -= 1
    elif direction == "s":
        current[1] += 1
    elif direction == "ne":
        current[0] += 1
        current[1] -= 1
    elif direction == "nw":
        current[0] -= 1
    elif direction == "se":
        current[0] += 1
    elif direction == "sw":
        current[0] -= 1
        current[1] += 1

    if max([abs(i) for i in current]) > maximum:
        maximum = max([abs(i) for i in current])
print(maximum)
