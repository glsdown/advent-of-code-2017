state = "A"
steps = 12208951
current = 0
tape_values = {current: False}
state_change_false = {
    "A": [1, "B"],
    "B": [-1, "C"],
    "C": [-1, "D"],
    "D": [-1, "E"],
    "E": [-1, "A"],
    "F": [-1, "E"],
}
state_change_true = {
    "A": [-1, "E"],
    "B": [1, "A"],
    "C": [1, "C"],
    "D": [-1, "F"],
    "E": [-1, "C"],
    "F": [1, "A"],
}

testing = False

# TEsting data
if testing:
    steps = 6
    state_change_false = {"A": [1, "B"], "B": [-1, "A"]}
    state_change_true = {"A": [-1, "B"], "B": [1, "A"]}

for i in range(steps):

    if current not in tape_values.keys():
        tape_values[current] = False

    previous_value = tape_values[current]

    if testing:
        if state in "A":
            tape_values[current] = not tape_values[current]
        elif state in "B":
            tape_values[current] = True
    else:
        if state in "ABCD":
            tape_values[current] = not tape_values[current]
        elif state in "EF":
            tape_values[current] = True

    if previous_value:
        current += state_change_true[state][0]
        state = state_change_true[state][1]
    elif not previous_value:
        current += state_change_false[state][0]
        state = state_change_false[state][1]


print(tape_values)
print(sum(x is True for x in list(tape_values.values())))
