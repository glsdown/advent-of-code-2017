passwords = []

with open("Day4Input.txt", "r") as f:
    for line in f:
        passwords.append(line.split())


valid = 0

for attempt in passwords:
    attempt = ["".join(sorted(i)) for i in attempt]  # included for round 2 only...
    duplicate = False
    for i in range(len(attempt)):
        if attempt[i] in attempt[i + 1 :]:
            duplicate = True
            break
    if not duplicate:
        valid += 1

print("There are", valid, "valid passcodes.")
