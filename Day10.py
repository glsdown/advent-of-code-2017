numbers = [i for i in range(256)]

current = 0
skip_size = 0

# Round 1
lengths = [46, 41, 212, 83, 1, 255, 157, 65, 139, 52, 39, 254, 2, 86, 0, 204]
# lengths = [3,4,1,5]


for length in lengths:
    # reverse order of elements
    list_to_reverse = numbers[current:] + numbers[:current]
    list_to_reverse = list_to_reverse[length - 1 :: -1]

    for counter in range(length):
        new_current = (current + counter) % len(numbers)
        numbers[new_current] = list_to_reverse[counter]

    current = (current + length + skip_size) % len(numbers)
    skip_size += 1

# print(numbers[0] * numbers[1])

# Round 2
current = 0
skip_size = 0
numbers = [i for i in range(256)]

string_lengths = "46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204"
# string_lengths = "1,2,4"
lengths = [ord(i) for i in string_lengths] + [17, 31, 73, 47, 23]

for _ in range(64):
    for length in lengths:
        # reverse order of elements
        list_to_reverse = numbers[current:] + numbers[:current]
        list_to_reverse = list_to_reverse[length - 1 :: -1]

        for counter in range(length):
            new_current = (current + counter) % len(numbers)
            numbers[new_current] = list_to_reverse[counter]

        current = (current + length + skip_size) % len(numbers)
        skip_size += 1

print(numbers)

dense_hash = []
row = 0
counter = 0
# numbers = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
for number in numbers:
    row ^= number
    counter += 1
    if counter % 16 == 0:
        dense_hash.append(row)
        row = 0
print(dense_hash)

hex_string = [str(hex(i))[2:] for i in dense_hash]
hash = ""
for item in hex_string:
    if len(item) == 1:
        hash += "0" + item
    else:
        hash += item
print(hash)
