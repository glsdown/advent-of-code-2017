# TEST CASE
gen_a_start = 65
gen_b_start = 8921

gen_a_start = 783
gen_b_start = 325

gen_a_factor = 16807
gen_b_factor = 48271

remainder = 2147483647
val = 2**16

count = 0


def make_gen_a():
    n = gen_a_start
    while True:
        n = (n * gen_a_factor) % remainder
        # Round 2 only:
        if n % 4 == 0:
            yield n


def make_gen_b():
    n = gen_b_start
    while True:
        n = (n * gen_b_factor) % remainder
        # Round 2 only:
        if n % 8 == 0:
            yield n


gen_a = make_gen_a()
gen_b = make_gen_b()

for i in range(5000000):
    if i % 1000000 == 0:
        print("Check:", i)

    if next(gen_a) % val == next(gen_b) % val:
        count += 1

print(count)
