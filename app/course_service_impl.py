from app.course_service import CourseService
from typing import List, Any
import math
import statistics


class CourseServiceImpl(CourseService):
    """
    Please implement the CourseService interface according to the requirements.
    """

    def __init__(self):
        self.courses = {}
        self.assignments = {}
        self.assignments_counter = 0
        self.courses_counter = 0

    def get_courses(self) -> List[Any]:
        """
        Returns a list of all courses.
        """
        allCourses = []
        for key, value in self.courses.items():
            allCourses.append({"id": key, "name":value["name"]})
        return allCourses

    def get_course_by_id(self, course_id) -> Any:
        """
        Returns a course by its id.
        """
        return (
            []
            if course_id not in self.courses
            else [{"id": course_id, "name":self.courses[course_id]["name"]}]
        )

    def create_course(self, course_name) -> int:
        """
        Creates a new course.
        Returns the id of the new course.
        """
        self.courses_counter += 1
        self.courses[self.courses_counter] = {"name": course_name, "students":{}}
        return self.courses_counter

    def delete_course(self, course_id) -> bool:
        """
        Deletes a course by its id.
        Returns True if the course was deleted successfully, otherwise False.
        """
        if course_id in self.courses:
            del self.courses[course_id]
            return True
        else:
            return False

    def create_assignment(self, course_id, assignment_name) -> int:
        """
        Creates a new assignment for a course.
        Returns the id of the new assignment.
        """
        if course_id in self.courses:
            self.assignments_counter += 1
            self.assignments[self.assignments_counter] = {"name": assignment_name, "course": course_id, "grades":[], "total_grade":0, "grade_count":0}
            return self.assignments_counter
        else:
            return 0

    def enroll_student(self, course_id, student_id) -> bool:
        """
        Enrolls a student in a course.
        Returns True if the student was enrolled successfully, otherwise False.
        """
        if course_id in self.courses:
            self.courses[course_id]["students"][student_id]=[]
            return True
        else:
            return False

    def dropout_student(self, course_id, student_id) -> bool:
        """
        Drops a student from a course.
        Returns True if the student was dropped successfully, otherwise False.
        """
        if course_id in self.courses and student_id in self.courses[course_id]["students"]:
            del self.courses[course_id]["students"][student_id]
            return True
        else:
            return False

    def submit_assignment(self, course_id, student_id, assignment_id, grade: int) -> bool:
        """
        Submits an assignment for a student. A grade of an assignment will be an integer between 0 and 100 inclusive.
        Returns True if the assignment was submitted successfully, otherwise False.
        """
        if course_id in self.courses and assignment_id in self.assignments and student_id in self.courses[course_id]["students"]:
            self.courses[course_id]["students"][student_id].append(grade)
            self.assignments[assignment_id]["grades"].append(grade)
            self.assignments[assignment_id]["total_grade"]+=grade
            self.assignments[assignment_id]["grade_count"]+=1
            return True
        else:
            return False

    def get_assignment_grade_avg(self, course_id, assignment_id) -> int:
        """
        Returns the average grade for an assignment. Floors the result to the nearest integer.
        """
        try:
            return math.floor(self.assignments[assignment_id]["total_grade"]/self.assignments[assignment_id]["grade_count"])
        except:
            return "There are no grades for this assignment"

    def get_student_grade_avg(self, course_id, student_id) -> int:
        """
        Returns the average grade for a student in a course. Floors the result to the nearest integer.
        """
        try:
          return math.floor(statistics.mean(self.courses[course_id]["students"][student_id] or [0]))
        except:
          return "Student or Course Doesn't exist"

    def get_top_five_students(self, course_id) -> List[int]:
        """
        Returns the IDs of the top 5 students in a course based on their average grades of all assignments.
        """
        if course_id not in self.courses or len(self.courses[course_id]["students"].keys())==0:
            return [0]
        averages = {key: statistics.mean(values or [0]) for key, values in self.courses[course_id]["students"].items()}
        sorted_data = dict(sorted(averages.items(), key=lambda x: -x[1]))
        return list(sorted_data.keys())[:5]

