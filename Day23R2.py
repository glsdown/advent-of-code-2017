a = 1
b = 65 * 100 + 100000
c = b + 17000
g = 0
h = 0

for b in range(65 * 100 + 100000, c + 1, 17):
    f = 1

    for d in range(2, b):
        if b % d == 0:
            f = 0
            break
        # for e in range(2, b):
        # if d*e == b:
        # f = 0
        # As d increases and e increases, need to check if d * e = b BEFORE e + 1 = b and d + 1 = b

    if f == 0:
        h += 1

print(h)
