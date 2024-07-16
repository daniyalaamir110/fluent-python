"""Unpacking Sequences

This module demonstrates the unpacking of sequences in Python. 

Unpacking allows us to assign the elements of a sequence to multiple variables in a 
single statement. We can unpack any iterable object like lists, tuples, strings, etc.
"""

import os
from collections import namedtuple
import datetime


def swapping_example():
    """Swapping Example

    This function demonstrates the use of unpacking to swap the values of two variables.
    """

    a = 10
    b = 20

    print(f"Before swapping: a = {a}, b = {b}")

    # Swapping the values of a and b
    # Non Pythonic way: Using a temporary variable
    # temp = a
    # a = b
    # b = temp

    # Pythonic way: Using unpacking
    a, b = b, a

    print(f"After swapping: a = {a}, b = {b}")


def reports_example():
    """Unpacking Reports Example

    This function demonstrates the use of unpacking to generate reports for students.
    """

    STUDENT_DATA_FILENAME = "08_student_data.txt"
    STUDENT_REPORT_TEMPLATE_FILENAME = "08_student_report_template.txt"
    STUDENT_REPORTS_DIR = "08_student_reports"
    PER_SUBJECT_MARKS = 100

    def get_student_data():
        """Get the student data

        Returns:
            `tuple`: The student records.
        """

        filepath = os.path.join(os.path.dirname(__file__), STUDENT_DATA_FILENAME)

        with open(filepath, "r") as file:

            # Use _ to ignore the header, and * to pack the rest of the lines into a list
            _, *body = file.readlines()

            raw_records = tuple(tuple(line.strip().split(", ")) for line in body)

            # Unpack the raw records to get the student ID, student name, and marks in order
            # to convert the numeric properties to integers.
            records = tuple(
                (int(student_id), student_name, *map(int, marks))
                for student_id, student_name, *marks in raw_records
            )

            return records

    def get_report_template():
        """Get the report template

        Returns:
            `str`: The report template string with data placeholders.
        """

        filepath = os.path.join(
            os.path.dirname(__file__), STUDENT_REPORT_TEMPLATE_FILENAME
        )

        with open(filepath, "r") as file:
            return file.read()

    def write_report_to_file(data, template):
        """Write the report to a file

        Args:
            data (`dict`): The data for the report.
            template (`str`): The template for the report.
        """

        student_id = data.get("student_id")
        student_name = data.get("student_name")

        filepath = os.path.join(
            os.path.dirname(__file__),
            STUDENT_REPORTS_DIR,
            f"{student_id:03}_{student_name}.txt",
        )

        with open(filepath, "w") as file:
            file.write(template.format(**data))

    def generate_report(record, template):
        """Generate the report for a student

        Creates a report for a student based on the record and the template.

        Args:
            record (`tuple`): The record of the student.
            template (`str`): The template for the report.

        Returns:
            `str`: The report info for the student.
        """

        student_id, name, *marks = record
        obtained_marks = sum(marks)
        total_marks = PER_SUBJECT_MARKS * len(marks)
        percentage = obtained_marks / total_marks * 100

        grade_map = ((80, "A+"), (70, "A"), (60, "B"), (50, "C"), (40, "D"))

        # Get the grade based on the percentage. We iterate through the grade_map
        # from the highest percentage to the lowest percentage and filter the grade
        # based on the percentage. Making use of generator expression will avoid the
        # need to evaluate all the valid grades at once. The we use the `next()` function
        # to get the first valid grade, and if we encounter the `StopIteration` exception,
        # consider the lowest i.e. "F" grade.
        grade = next((grade for tresh, grade in grade_map if percentage >= tresh), "F")

        maths, english, physics, chemistry, art = marks

        # The `strftime` method is used to format a date object as a string as we want.
        report_generation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "student_id": student_id,
            "student_name": name,
            "maths": maths,
            "english": english,
            "physics": physics,
            "chemistry": chemistry,
            "art": art,
            "obtained_marks": obtained_marks,
            "total_marks": total_marks,
            "percentage": percentage,
            "grade": grade,
            "report_generation_time": report_generation_time,
        }

        write_report_to_file(data, template)

        return (
            f"Student ID: {student_id:03},\tName: {name}\tTotal Marks: {obtained_marks}"
        )

    records = get_student_data()
    template = get_report_template()
    reports = tuple(generate_report(record, template) for record in records)
    print("\n".join(reports))


def gcd_example():
    """GCD Example

    This function demonstrates the use of unpacking to calculate the GCD of two numbers.
    """

    def eucliedean_gcd(a, b):
        """Calculate the GCD of two numbers

        Makes use of the Euclidean algorithm to calculate the GCD of two numbers.

        Args:
            a (`int`): The first number.
            b (`int`): The second number.

        Returns:
            `int`: The GCD of the two numbers.
        """

        while b:
            a, b = b, a % b
        return a

    def gcd(a, *nums):
        """Calculate the GCD of multiple numbers

        Args:
            nums (`tuple`): The numbers.

        Returns:
            `int`: The GCD of the numbers.
        """

        # Could have also used only *nums in the function signature
        # but `a` is made a positional argument to avoid the case where
        # the function is called with no arguments because `gcd` requires
        # at least one argument.

        # If one number is passed, return the number itself
        if not nums:
            return a

        # Use unpacking to get the second number `b`
        b, *rest = nums

        current_gcd = eucliedean_gcd(a, b)

        # Recursively calculate the GCD of the rest of the numbers
        # until all numbers are exhausted and return the GCD.
        return gcd(current_gcd, *rest) if rest else current_gcd

    expression = "gcd(10, 20, 30, 40, 50)"
    print(f"{expression} = {eval(expression)}")


if __name__ == "__main__":
    swapping_example()
    reports_example()
    gcd_example()
