# Set up the starting values
duet = {}
duet_1 = {}
instructions = []
current = [0]

with open("Day18Input.txt", "r") as f:
    for line in f:
        instructions.append(line.split())

registers = list(set([i[1] for i in instructions]))

for register in registers:
    if not register.isdigit():
        duet[register] = 0


def snd(x):
    current[0] = duet[x]


def setting(x, y):
    try:
        duet[x] = int(y)
    except ValueError:
        duet[x] = duet[y]


def adding(x, y):
    try:
        val = int(y)
        duet[x] += val
    except ValueError:
        duet[x] += duet[y]


def mul(x, y):
    try:
        val = int(y)
        duet[x] *= val
    except ValueError:
        duet[x] *= duet[y]


def mod(x, y):
    try:
        val = int(y)
        duet[x] %= val
    except ValueError:
        duet[x] %= duet[y]


def rcv(x):
    if duet[x] == "0":
        return False
    else:
        return current[0]


def jgz(x, y):
    try:
        x = int(x)
    except ValueError:
        x = int(duet[x])
    if x > 0:
        offset = int(y)
        return offset
    else:
        return 1


i = 0

while True:
    current_instruction = instructions[i][0]
    # print("Current Instruction =", current_instruction)
    if current_instruction == "snd":
        snd(instructions[i][1])
    elif current_instruction == "rcv":
        result = rcv(instructions[i][1])
        if result:
            print(duet)
            print(result)
            break
    elif current_instruction == "set":
        setting(instructions[i][1], instructions[i][2])
    elif current_instruction == "add":
        adding(instructions[i][1], instructions[i][2])
    elif current_instruction == "mul":
        mul(instructions[i][1], instructions[i][2])
    elif current_instruction == "mod":
        mod(instructions[i][1], instructions[i][2])
    # print(instructions[i], "gave", duet)
    if current_instruction == "jgz":
        i += jgz(instructions[i][1], instructions[i][2])
    else:
        i += 1
