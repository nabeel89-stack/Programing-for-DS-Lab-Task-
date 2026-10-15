marks = [75, 82, 48, 91, 66]

total = sum(marks)
average = total / len(marks)
passed = 0
for m in marks:
    if m >= 50:
        passed += 1

print("Total:", total)
print("Average:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Passed courses:", passed)
