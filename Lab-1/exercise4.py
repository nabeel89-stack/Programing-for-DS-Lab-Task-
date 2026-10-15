name = input("Enter student name: ")
m1 = float(input("Enter mark 1: "))
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))
m4 = float(input("Enter mark 4: "))
m5 = float(input("Enter mark 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5
highest = max(m1, m2, m3, m4, m5)
lowest = min(m1, m2, m3, m4, m5)
passed = 0
for m in (m1, m2, m3, m4, m5):
    if m >= 50:
        passed += 1

print("Student:", name)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed courses:", passed)
