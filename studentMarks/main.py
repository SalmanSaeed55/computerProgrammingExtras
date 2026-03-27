"""Module for entering student marks and displaying summary."""


def enter_student_marks():
    """Enter student marks interactively.

    Returns:
        dict: Dictionary of student names to marks.
    """
    student_marks = {}
    while True:
        try:
            name = input("Enter student name (or 'done' to finish): ").strip()

            if name.lower() == "done":
                break

            if not name:
                print("Student name cannot be empty. Please try again.")
                continue

            mark = float(input(f"Enter mark for {name}: "))

            if 0 <= mark <= 100 and mark:
                student_marks[name] = mark
            else:
                print("Invalid mark. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid mark.")
    return student_marks


def marks_summary(marks_dict):
    """Display summary of student marks: average and top student.

    Args:
        marks_dict (dict): Dictionary of student names to marks.
    """
    top_student = ""
    if not marks_dict:
        print("No student marks to display.")
        return

    total_marks = sum(marks_dict.values())
    top_student_mark = max(marks_dict.values())

    for name, mark in marks_dict.items():
        if mark == top_student_mark:
            top_student = name

    print("\n----- Class Summary -----")
    print(f"Average marks: {round(total_marks / len(marks_dict), 2)}")
    print(f"Top student: {top_student}")


if __name__ == "__main__":
    marks = enter_student_marks()
    marks_summary(marks)
