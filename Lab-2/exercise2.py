temps = (28, 31, 30, 27, 29, 32)

highest = temps[0]
lowest = temps[0]
for t in temps:
    print("Reading:", t)
    if t > highest:
        highest = t
    if t < lowest:
        lowest = t

print("Highest:", highest)
print("Lowest:", lowest)
