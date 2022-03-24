ports = []

with open("Day24Input.txt", "r") as file:
    for line in file:
        ports.append(sorted([int(i) for i in line.strip().split("/")]))

ports.sort()

start = ports[0]
available = [i for i in ports[1:]]

# ROUND 2
def get_bridge(value, available_ports, position, length):

    values_to_check = [l for l in available_ports if value[position] in l]

    if len(values_to_check) == 0:
        return start[1], length
    else:
        max_score = 0
        max_length = 0
        for new_value in values_to_check:
            new_value_index = available_ports.index(new_value)
            if new_value[0] == value[position]:
                new_position = 1
            elif new_value[1] == value[position]:
                new_position = 0
            current_score, new_length = get_bridge(
                new_value,
                available_ports[:new_value_index]
                + available_ports[new_value_index + 1 :],
                new_position,
                length + 1,
            )
            current_score += sum(new_value)
            if new_length > max_length:
                max_length = new_length
                max_score = current_score
            elif new_length == max_length and current_score > max_score:
                max_score = current_score
        return max_score, max_length


print(get_bridge(start, available, 1, 1))

# ROUND 1
def find_bridge(value, available_ports, position):
    values_to_check = [l for l in available_ports if value[position] in l]
    if len(values_to_check) == 0:
        return start[1]
    else:

        maximum = 0
        for new_value in values_to_check:
            new_value_index = available_ports.index(new_value)
            if new_value[0] == value[position]:
                new_position = 1
            elif new_value[1] == value[position]:
                new_position = 0
            current = sum(new_value) + find_bridge(
                new_value,
                available_ports[:new_value_index]
                + available_ports[new_value_index + 1 :],
                new_position,
            )
            if current > maximum:
                maximum = current
        return maximum


# print(find_bridge(start, available, 1))
