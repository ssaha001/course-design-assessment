from app.course_service_impl import CourseServiceImpl

def test_create_course():
    course_service = CourseServiceImpl()
    assert(course_service.create_course("Introduction to C++")) == 1, "Create Course test failed"
    assert(course_service.create_course("Introduction to Python")) == 2, "Create Course test failed"

def test_get_courses():
    course_service = CourseServiceImpl()
    assert len(course_service.get_courses()) == 0, "Get Course test failed"
    course_service.create_course("Introduction to C++")
    course_service.create_course("Introduction to Python")
    assert len(course_service.get_courses()) == 2, "Get Course test failed"

def test_get_course_by_id():
    course_service = CourseServiceImpl()
    course_service.create_course("Introduction to C++")
    course_service.create_course("Introduction to Python")
    assert len(course_service.get_courses()) == 2, "Get Course by id test failed"
    assert len(course_service.get_course_by_id(1)) == 1, "Get Course by id test failed"
    assert course_service.get_course_by_id(1)[0]["name"] == "Introduction to C++", "Get Course by id test failed"
    assert course_service.get_course_by_id(2)[0]["name"] == "Introduction to Python", "Get Course by id test failed"

def test_delete_courses():
    course_service = CourseServiceImpl()
    course_service.create_course("Introduction to C++")
    assert course_service.delete_course(1) == True, "Delete Course test failed"
    assert course_service.delete_course(2) == False, "Delete Course test failed"

def test_enroll_dropout_student():
    course_service = CourseServiceImpl()
    course_service.create_course("Introduction to C++")
    assert(course_service.enroll_student(1,1))==True, "Enroll Dropout Student test failed"
    assert(course_service.enroll_student(2,1))==False, "Enroll Dropout Student test failed"
    assert(course_service.dropout_student(1,1))==True, "Enroll Dropout Student test failed"
    assert(course_service.dropout_student(1,1))==False, "Enroll Dropout Student test failed"

def test_create_assignment():
    course_service = CourseServiceImpl()
    assert(course_service.create_assignment(1,"Assignment 1"))==0, "Create Assignment test failed"
    course_service.create_course("Introduction to C++")
    assert(course_service.create_assignment(1,"Assignment 1"))==1, "Create Assignment test failed"

def test_submit_assignment():
    course_service = CourseServiceImpl()
    assert(course_service.submit_assignment(1,1,1,100))==False, "Submit Assignment test failed"
    course_service.create_course("Introduction to C++")
    assert(course_service.submit_assignment(1,1,1,100))==False, "Submit Assignment test failed"
    course_service.enroll_student(1,1)
    assert(course_service.submit_assignment(1,1,1,100))==False, "Submit Assignment test failed"
    course_service.create_assignment(1,"Assignment 1")
    assert(course_service.submit_assignment(1,1,1,100))==True, "Submit Assignment test failed"

def test_get_grades():
    course_service = CourseServiceImpl()
    course_service.create_course("Introduction to C++")
    assert(course_service.get_student_grade_avg(2,1)) == "Student or Course Doesn't exist", "Test get_student_grade_avg failed"
    assert(course_service.get_assignment_grade_avg(1,1)) == "There are no grades for this assignment", "Test get_assignment_grade_avg failed"
    assert(course_service.get_student_grade_avg(1,1)) == "Student or Course Doesn't exist", "Test get_student_grade_avg failed"
    course_service.create_assignment(1,"Assignment 1")
    course_service.create_assignment(1,"Assignment 2")
    course_service.create_assignment(1,"Assignment 3")
    course_service.enroll_student(1,1)
    assert(course_service.get_student_grade_avg(1,1)) == 0, "Test get_student_grade_avg failed"
    course_service.enroll_student(1,2)
    course_service.enroll_student(1,3)
    course_service.enroll_student(1,4)
    course_service.enroll_student(1,5)
    course_service.enroll_student(1,6)
    # Student 1
    course_service.submit_assignment(1,1,1,20)
    course_service.submit_assignment(1,1,2,30)
    course_service.submit_assignment(1,1,3,40)
    # Student 2
    course_service.submit_assignment(1,2,1,30)
    course_service.submit_assignment(1,2,2,60)
    course_service.submit_assignment(1,2,3,60)
    # Student 3
    course_service.submit_assignment(1,3,1,13)
    course_service.submit_assignment(1,3,2,0)
    course_service.submit_assignment(1,3,3,80)
    # Student 4
    course_service.submit_assignment(1,4,1,3)
    course_service.submit_assignment(1,4,2,0)
    course_service.submit_assignment(1,4,3,10)
    # Student 5
    course_service.submit_assignment(1,5,1,30)
    course_service.submit_assignment(1,5,2,90)
    course_service.submit_assignment(1,5,3,100)
    # Student 6
    course_service.submit_assignment(1,6,1,0)
    course_service.submit_assignment(1,6,2,0)
    course_service.submit_assignment(1,6,3,7)

    assert(course_service.get_student_grade_avg(1,1)) == 30, "Test get_student_grade_avg failed"
    assert(course_service.get_assignment_grade_avg(1,1)) == 16, "Test get_assignment_grade_avg failed"
    assert(course_service.get_top_five_students(1)) == [5,2,3,1,4], "Test get_top_five_students failed"
    assert(course_service.get_top_five_students(2)) == [0], "Test get_top_five_students failed"
    assert(course_service.get_student_marks_for_assignment(1,6,3)) == 7, "Test get_student_marks_for_assignment failed"
    assert(course_service.get_student_marks_for_assignment(1,6,7)) == "Grades for this assignment doesn't exist", "Test get_student_marks_for_assignment failed"

try:
    test_create_course()
    test_get_courses()
    test_get_course_by_id()
    test_enroll_dropout_student()
    test_create_assignment()
    test_submit_assignment()
    test_get_grades()
    print("All tests passed!")
except AssertionError as e:
    print(f"Test failed: {e}")
