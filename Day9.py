with open("Day9Input.txt", "r") as f:
    stream = f.read()

print(stream)

in_group = False
in_garbage = False
negate = False
score = 0
current_level = 0
num_chars = 0

for character in stream:
    if negate:
        negate = False
    else:
        if character == "!":
            negate = True
        elif not in_garbage:
            if character == "{":
                in_group = True
                current_level += 1
                score += current_level
            elif character == "}" and in_group:
                current_level -= 1
                if current_level == 0:
                    in_group = False
            elif character == "<":
                in_garbage = True
        else:
            if character == ">":
                in_garbage = False
            else:
                num_chars += 1

# Round 1
print(score)

# Round 2
print(num_chars)
