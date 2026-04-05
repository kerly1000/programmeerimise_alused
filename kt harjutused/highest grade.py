def show_highest_grade(grade1: int, grade2: int) -> None:
    """
    Print "Highest grade: GRADE" where GRADE is the higher of two inputs.

    grade1, grade2 are both non-negative integers.

    3, 4 => "Highest grade: 4"
    1, 2 => "Highest grade: 1"
    """
    if grade1 > grade2:
        print (f"Highest grade: {grade1}")
    else:
        print (f"Highest grade: {grade2}")


    highest = max(grade1, grade2)
    print(f"Highest grade: {highest}")