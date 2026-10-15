def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


marks = [78, 85, 69, 90, 72]
print("Grade:", calculate_grade(marks))
