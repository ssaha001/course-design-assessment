from app.course_service_impl import CourseServiceImpl

if __name__ == "__main__":
  course_service = CourseServiceImpl()

  # Start receiving requests...
  print(course_service.create_course("CCP555"))
  print(course_service.get_courses())
  print(course_service.get_course_by_id(1))
  print(course_service.enroll_student(1,1))
  print(course_service.get_student_grade_avg(1,1))
