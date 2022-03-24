# Get instructions
instructions = []
with open("Day18Input.txt", "r") as f:
    for line in f:
        instructions.append(line.split())

# Set up registers
registers = {}
unique = list(set([i[1] for i in instructions]))
for register in unique:
    if not register.isdigit():
        registers[register] = [0, 0]
registers["p"] = [0, 1]

# set up the queue
queue = {0: [], 1: []}

# Send value to the queue
def snd(x, program):
    try:
        x = int(x)
    except ValueError:
        x = int(registers[x][program])
    queue[(program + 1) % 2].append(x)


# Receive value from the queue
def rcv(x, program):
    registers[x][program] = queue[program][0]
    queue[program].pop(0)


# Jump operation
def jgz(x, y, program):
    # Work out whether x is location or value
    try:
        x = int(x)
    except ValueError:
        x = int(registers[x][program])

    # Work out whether y is location or value
    try:
        y = int(y)
    except ValueError:
        y = int(registers[y][program])

    # Calculate the 'jump' needed
    if x > 0:
        return y
    else:
        return 1


# Other operations on values
def arithmetic(option, x, y, program):
    # Work out whether y is a location or a value
    try:
        y = int(y)
    except ValueError:
        y = int(registers[y][program])

    # Carry out the operation
    if option == "set":
        registers[x][program] = y
    elif option == "add":
        registers[x][program] += y
    elif option == "mul":
        registers[x][program] *= y
    elif option == "mod":
        registers[x][program] %= y


# Run program
current = [0, 0]
program = 1
deadlock = [False, False]
count = [0, 0]

while True:
    # Find the current instruction
    current_instruction = instructions[current[program]][0]
    x = instructions[current[program]][1]
    try:
        y = instructions[current[program]][2]
    except IndexError:
        y = 0

    # Check if sending value to the queue
    if current_instruction == "snd":
        deadlock[(program + 1) % 2] = False
        count[program] += 1
        snd(x, program)
    # Check if receiving value from the queue
    elif current_instruction == "rcv":
        if len(queue[program]) == 0:
            deadlock[program] = True
            current[program] -= 1
        else:
            rcv(x, program)
    elif current_instruction != "jgz":
        arithmetic(current_instruction, x, y, program)

    # Get the next instruction.
    if current_instruction == "jgz":
        current[program] += jgz(x, y, program)
    else:
        current[program] += 1

    # Go back to the next program
    program = (program + 1) % 2
    if deadlock[program]:
        # If that program is in deadlock, switch back to original
        program = (program + 1) % 2

    # Checks whether both programs are stuck
    if all(deadlock):
        print("Deadlock reached!")
        print(current)
        print("Program 0 sent", count[0], "instructions")
        print("Program 1 sent", count[1], "instructions")
        break
