students_list = {}
course_list = {}

def input_no_student():
    num_student = int(input("Enter number of student(s) in a class:"))
    print("There are", num_student, "in the class")
    return num_student


def input_no_courses():
    num_courses = int(input("Enter number of courses: "))
    print("There are", num_courses, "courses")
    return num_courses


def registerCourses(course):
    course_id = input("Enter course's id: ")
    course_name = input("Enter course's name: ")
    course_list[course_id] = course_name

def input_student_info(stu_number):
    print("Enter infos for student number",stu_number)
    student_id = input("Enter student's id: ")
    student_name = input("Enter student's name: ")
    student_DoB = input("Enter student's DoB: ")
    student_info = {"Name": student_name, "DoB": student_DoB}
    students_list[student_id] = student_info

def inputMarks(course,stu):
    marks = input("Grade the student performance on the course:")


def main():
    amount_student = input_no_student()
    amount_course = input_no_courses()

    for x in range(amount_student):
        input_student_info(x)

    

main()
