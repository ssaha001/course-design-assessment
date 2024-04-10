from app.course_service_impl import CourseServiceImpl


#All functions take a db parameter cause I didn't want to change the existing code and move course_service from main file to this one.

def add_course_prompt(db: CourseServiceImpl):
    course_name=str(input("Enter course name: "))
    course_id=db.create_course(course_name)
    print("     \nId of the created course is: ", course_id)
    print("-"*60)

def delete_course_prompt(db: CourseServiceImpl):
    course_id=int(input("Enter course number: "))
    if db.delete_course(course_id):
        print("     \nCourse Successfully Deleted")
    else:
        print("     \nCouldn't delete the course")
    print("-"*60)

def view_all_courses_prompt(db: CourseServiceImpl):
    courses= db.get_courses()
    if len(courses)>0:
        for course in courses:
            print(f"    \nCourse Name: {course['name']} Course Id: {course['id']}")
    else:
        print("\n   There are no courses")
    print("-"*60)

def view_specific_courses_prompt(db: CourseServiceImpl):
    course_id=int(input("Enter course id: "))
    courses= db.get_course_by_id(course_id)
    if len(courses)>0:
            print(f"\n  Course Name: {courses[0]['name']} Course Id: {courses[0]['id']}")
    else:
        print("\n   There are no courses")
    print("-"*60)

def enroll_student_prompt(db: CourseServiceImpl):
    course_id=int(input("Enter course id: "))
    student_id=int(input("Enter student id: "))
    
    if db.enroll_student(course_id,student_id):
            print("\n   Student added to course")
    else:
        print("\n   Course Doesn't exist")
    print("-"*60)

def drop_student_prompt(db: CourseServiceImpl):
    course_id=int(input("Enter course id: "))
    student_id=int(input("Enter student id: "))
    
    if db.dropout_student(course_id,student_id):
            print("\n   Student removed from course")
    else:
        print("\n   Student not enrolled in this course")
    print("-"*60)

def create_assignment_prompt(db: CourseServiceImpl):
    course_id=int(input("Enter course id: "))
    assignment_name=str(input("Enter assignemnt name: "))
    
    assignment_id=db.create_assignment(course_id, assignment_name)
    if assignment_id==0:
            print("\n   Course Doesn't Exist")
    else:
        print("\n   Id of the created assignment is ", assignment_id)
    print("-"*60)

def submit_assignment_prompt(db: CourseServiceImpl):
    course_id=int(input("Enter course id: "))
    student_id=int(input("Enter student id: "))
    assignment_id=int(input("Enter assignment id: "))
    grade=float(input("Enter Grade: "))
    
    if db.submit_assignment(course_id,student_id, assignment_id, grade):
            print("\n   Assignment Submitted")
    else:
        print("\n   ERROR! Student, Assignment, or Course does not exist")
    print("-"*60)

def view_student_average_prompt(db: CourseServiceImpl):
    course_id=int(input("Enter course id: "))
    student_id=int(input("Enter student id: "))

    average= db.get_student_grade_avg(course_id,student_id)
    print("\n   Student's average grade in this course is: "if type(average)==int else "\n    ",average)
    print("-"*60)

def view_assignment_average_prompt(db: CourseServiceImpl):
    course_id=int(input("Enter course id: "))
    assignment_id=int(input("Enter assignment id: "))

    average= db.get_assignment_grade_avg(course_id,assignment_id)
    print("\n  Assignment's average grade is: " if type(average)==int else "\n    ",average)
    print("-"*60)

def top_five_students_prompt(db: CourseServiceImpl):
    course_id=int(input("Enter course id: "))

    top_five=db.get_top_five_students(course_id)
    if 0 in top_five:
        print("\n   There are no students enrolled in this course")
    else:
        print("\n   Top 5 students are:")
        for student_id in top_five:
            print("\n   Student Id: ", student_id)
    print("-"*60)

def view_student_assignment_grade_prompt(db: CourseServiceImpl):
    course_id=int(input("Enter course id: "))
    assignment_id=int(input("Enter assignment id: "))
    student_id=int(input("Enter student id: "))

    grade= db.get_student_marks_for_assignment(course_id,student_id,assignment_id)
    print("\n   Grade for selected assignment is: " if type(grade)==float else "\n    ",grade)
    print("-"*60)