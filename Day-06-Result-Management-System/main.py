import random


def generate_student_id():
    """Generate a random Student ID."""
    return f"STD{random.randint(1000, 9999)}"


def get_student_details():
    """Get student details."""

    print("=" * 65)
    print("          📚 SSC STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 65)

    student_name = input("\nEnter Student Name: ")

    return student_name


def get_student_marks(subjects):
    """Get marks for all subjects."""

    marks = []

    print("\nEnter Marks (Out of 100)\n")

    for subject in subjects:

        while True:

            try:
                mark = int(input(f"{subject}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break

                print("❌ Marks must be between 0 and 100.")

            except ValueError:
                print("❌ Please enter a valid number.")

    return marks


def calculate_percentage(marks):
    """Calculate total marks and percentage."""

    total_marks = sum(marks)
    maximum_marks = len(marks) * 100

    percentage = (total_marks / maximum_marks) * 100

    return total_marks, percentage


def calculate_grade(percentage):
    """Calculate grade based on percentage."""

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B+"

    elif percentage >= 60:
        return "B"

    elif percentage >= 50:
        return "C"

    elif percentage >= 35:
        return "D"

    return "F"


def calculate_result(subjects, marks):
    """Check PASS / FAIL."""

    failed_subjects = []

    for subject, mark in zip(subjects, marks):

        if mark < 35:
            failed_subjects.append(subject)

    if failed_subjects:
        return "FAIL", failed_subjects

    return "PASS", failed_subjects


def display_report_card(
        student_id,
        student_name,
        subjects,
        marks,
        total_marks,
        percentage,
        grade,
        result,
        failed_subjects
):
    """Display Student Report Card."""

    print("\n")
    print("=" * 65)
    print("                 📑 SSC STUDENT REPORT CARD")
    print("=" * 65)

    print(f"Student ID   : {student_id}")
    print(f"Student Name : {student_name}")

    print("-" * 65)
    print(f"{'Subject':<35}{'Marks'}")
    print("-" * 65)

    for subject, mark in zip(subjects, marks):
        print(f"{subject:<35}{mark}")

    print("-" * 65)

    if result == "PASS":

        print(f"Total Marks  : {total_marks} / 600")
        print(f"Percentage   : {percentage:.2f}%")
        print(f"Grade        : {grade}")
        print(f"Result       : ✅ PASS")

    else:

        print("Result       : ❌ FAIL")
        print()

        print("Reason:")
        print("The student has failed in the following subject(s):")

        for subject in failed_subjects:
            print(f"• {subject}")

        print()
        print("Total Marks  : N/A")
        print("Percentage   : N/A (Student has not passed all subjects)")
        print("Grade        : N/A")

    print("=" * 65)


def main():

    subjects = [
        "English",
        "Hindi",
        "Mathematics",
        "Science",
        "Social Science",
        "Computer Science"
    ]

    student_id = generate_student_id()

    student_name = get_student_details()

    marks = get_student_marks(subjects)

    result, failed_subjects = calculate_result(subjects, marks)

    if result == "PASS":

        total_marks, percentage = calculate_percentage(marks)
        grade = calculate_grade(percentage)

    else:

        total_marks = None
        percentage = None
        grade = None

    display_report_card(
        student_id,
        student_name,
        subjects,
        marks,
        total_marks,
        percentage,
        grade,
        result,
        failed_subjects
    )



main()