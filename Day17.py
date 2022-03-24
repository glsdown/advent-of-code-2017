import blist

spinlock = blist.blist([0])
step = 303
position = 0


for i in range(1, 50000000):
    if i % 1000000 == 0:
        print("Round:", i)
    position = (position + step) % len(spinlock) + 1
    spinlock.insert(position, i)

print(spinlock[spinlock.index(0) + 1])
