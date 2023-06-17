def calculate_gpa():
    subjects = {
        'edc': 3,
        'dld': 2,
        'ss': 3,
        'ptsp': 3,
        'ttnm': 3,
        'uhv': 3,
        'sos': 2,
        'edclab': 1,
        'bslab': 1,
        'dldlab': 1,
        'ts': 1,
        'cvv': 1
    }

    total_credits = sum(subjects.values())
    total_grade_points = 0

    for subject, credits in subjects.items():
        marks = int(input(f"Enter marks for {subject}: "))
        grade = calculate_grade(marks)
        grade_points = grade * credits
        total_grade_points += grade_points

    gpa = total_grade_points / total_credits
    return gpa


def calculate_grade(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    elif marks >= 40:
        return 5
    elif marks >= 30:
        return 4
    elif marks >= 20:
        return 3
    elif marks >= 10:
        return 2
    else:
        return 1


gpa = calculate_gpa()
print(f"Your GPA is: {gpa}")
