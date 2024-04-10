from app.course_service_impl import CourseServiceImpl
from prompts import add_course_prompt, delete_course_prompt, view_all_courses_prompt, view_specific_courses_prompt, enroll_student_prompt, drop_student_prompt, create_assignment_prompt, submit_assignment_prompt, view_student_average_prompt, view_assignment_average_prompt, top_five_students_prompt
def print_options():
  print("1) Add Course\n2) View all Coursenames\n3) View Coursename by id\n4) Delete Course\n5) Enroll Student\n6) Dropout Student\n7) Create Assignemnt\n8) Submit Assignment\n9) View student average\n10) View assignment average\n11) View top 5 students of course\n0) Exit")

prompts={
  1: add_course_prompt,
  2: view_all_courses_prompt,
  3: view_specific_courses_prompt,
  4: delete_course_prompt,
  5: enroll_student_prompt,
  6: drop_student_prompt,
  7: create_assignment_prompt,
  8: submit_assignment_prompt,
  9: view_student_average_prompt,
  10: view_assignment_average_prompt,
  11: top_five_students_prompt
}

if __name__ == "__main__":
  course_service = CourseServiceImpl()
  first_option=-1
  while first_option !=0:
    print_options()
    first_option=int(input("Enter your choice: "))
    while first_option not in range(0,12):
      first_option=int(input("Please enter a number from above list: "))
    if first_option == 0:
      break
    else:
      prompts[first_option](course_service)

  print("-"*40)
  print("Thanks for testing!")
  
