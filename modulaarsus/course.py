"""Course module."""
from typing import Dict
from student import Student
import statistics
class Course:
    def __init__(self, name: str):
        """Initialize course object with name."""
        self.__name = name
        self.__grades: Dict[Student, int] = {}

    def get_grades(self) -> list [tuple[Student, int]]:
        """Return a list of"""
        return list(self.__grades.items())

    def get_average_grade(self) -> float:
        """Return the average grade of al student grades."""
        if len(self.__grades) == 0:
            return -1
        return statistics.mean(self.__grades.values())

    def __repr__(self) -> str:
        return
