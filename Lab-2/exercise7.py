students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78},
]

passed = 0
total = 0
top = students[0]
for s in students:
    print(s["name"], s["marks"])
    total += s["marks"]
    if s["marks"] >= 50:
        passed += 1
    if s["marks"] > top["marks"]:
        top = s

print("Passed students:", passed)
print("Class average:", total / len(students))
print("Highest mark:", top["name"], top["marks"])
