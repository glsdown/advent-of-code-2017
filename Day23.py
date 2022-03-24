# Set up the starting values
registers = {}
instructions = []
current = [0]

with open("Day23InputNEW.txt", "r") as f:
    for line in f:
        instructions.append(line.split())

print(instructions)

for letter in "abcdefgh":
    registers[letter] = 0

registers["a"] = 1


def setting(x, y):
    try:
        registers[x] = int(y)
    except ValueError:
        registers[x] = registers[y]


def subtract(x, y):
    try:
        registers[x] -= int(y)
    except ValueError:
        registers[x] -= registers[y]


def mul(x, y):
    try:
        registers[x] *= int(y)
    except ValueError:
        registers[x] *= registers[y]


def jnz(x, y):
    try:
        x = int(x)
    except ValueError:
        x = int(registers[x])
    if x != 0:
        offset = int(y)
        return offset
    else:
        return 1


i = 0
counter = 0

try:
    while True:
        current_instruction = instructions[i][0]
        if current_instruction == "set":
            setting(instructions[i][1], instructions[i][2])
        elif current_instruction == "sub":
            subtract(instructions[i][1], instructions[i][2])
        elif current_instruction == "mul":
            mul(instructions[i][1], instructions[i][2])
            counter += 1
        if current_instruction == "jnz":
            i += jnz(instructions[i][1], instructions[i][2])
        else:
            i += 1
        print(i)
except IndexError:
    print("Mul was invoked", counter, "times")
    print(registers)
