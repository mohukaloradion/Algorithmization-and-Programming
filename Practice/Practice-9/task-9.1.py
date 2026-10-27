def calculate_average(grades):
    if not grades:
        return 0.0
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

def find_highest_grade(grades):
    if not grades:
        return None
    highest = grades[0]
    for grade in grades:
        if grade > highest:
            highest = grade
    return highest

def analyze_student_performance(grades):
    avg = calculate_average(grades)
    highest = find_highest_grade(grades)
    return avg, highest

student_grades = [85, 92, 78, 90, 88]
average_grade, top_grade = analyze_student_performance(student_grades)

print(f"Аналізовані оцінки: {student_grades}")
print(f"Середній бал: {average_grade:.2f}")
print(f"Найвища оцінка: {top_grade}")
