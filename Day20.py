# ROUND 2

particles = {}

with open("Day20Input.txt", "r") as f:
    count = 0
    for line in f:
        text = line.strip().split(", ")
        particle = {}
        for prop in text:
            values = prop.split(",")
            value0 = values[0].split("=<")
            name = value0[0]
            x = value0[1]
            y = values[1]
            z = values[2][:-1]
            particle[name] = [int(x), int(y), int(z)]
        particles[count] = particle
        count += 1
print(particles)

counter = 1

while counter < 500:

    duplicate = set()
    unique = set()
    # Update the values
    for k in particles.keys():
        for j in range(3):
            particles[k]["v"][j] += particles[k]["a"][j]
            particles[k]["p"][j] += particles[k]["v"][j]
        if tuple(particles[k]["p"]) in unique:
            duplicate.add(tuple(particles[k]["p"]))
        else:
            unique.add(tuple(particles[k]["p"]))

    unique = unique - duplicate

    keystoremove = []
    for k in particles.keys():
        if tuple(particles[k]["p"]) not in unique:
            keystoremove.append(k)

    for key in keystoremove:
        particles.pop(key)

    print("There are", len(particles.keys()), "particles left after round", counter)
    counter += 1


# ROUND 1
"""

particles = []

with open("Day20Input.txt", "r") as f:
    for line in f:
        text = line.strip().split(", ")
        particle = {}
        for prop in text:
            values = prop.split(",")
            value0 = values[0].split("=<")
            name = value0[0]
            x = value0[1]
            y = values[1]
            z = values[2][:-1]
            particle[name] = [int(x), int(y), int(z)]
        particles.append(particle)
print(particles)

def manhatten(my_list):
    return sum([abs(i) for i in my_list])

for i in range(5000):
    minimum = manhatten(particles[0]["p"])
    minimum_particle = 0
    for k in range(len(particles)):
        for j in range(3):
            particles[k]["v"][j] += particles[k]["a"][j]
            particles[k]["p"][j] += particles[k]["v"][j]
        distance = manhatten(particles[k]["p"])
        if distance < minimum:
            minimum = distance
            minimum_particle = k

    if i%1000== 0:
        print("Round", i,":", minimum, "from", minimum_particle)
"""
