def find_maxmimum(my_list):
    maximum = 0
    max_index = 0
    for index in range(len(my_list)):
        if my_list[index] > maximum:
            maximum = my_list[index]
            max_index = index
    return max_index


def redistribute(my_list, index):
    value = my_list[index]
    my_list[index] = 0
    each_block = (value // len(my_list)) + 1
    left_over = len(my_list) - (value % len(my_list))

    for counter in range(len(my_list)):
        current = (1 + counter + index) % len(my_list)
        my_list[current] += each_block
    for counter in range(left_over):
        current = (index - counter) % len(my_list)
        my_list[current] -= 1
    return my_list


blocks = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]
# blocks = [0, 2, 7, 0]
blocks_in_banks = []
blocks_in_banks.append([i for i in blocks])
count = 0

# Round 1
while True:

    my_max = find_maxmimum(blocks)
    blocks = redistribute(blocks, my_max)
    if blocks in blocks_in_banks:
        block_to_find = [i for i in blocks]
        while True:
            count += 1
            my_max = find_maxmimum(blocks)
            blocks = redistribute(blocks, my_max)
            if blocks == block_to_find:
                break
        break
    else:
        blocks_in_banks.append([i for i in blocks])

print("Took", count, "goes")
