student_list = []
course_list = []
marks = {}

import time
import os

class Course:
    def __init__(self,id,name):
        self.__id = id
        self.__name = name

    def _get_course_info(self):
        return self.__id,self.__name
    
    def _get_course_id(self):
        return self.__id
    
    def _get_course_name(self):
        return self.__name

class Student:
    def __init__(self,id,name,DoB):
        self.__id = id
        self.__name = name
        self.__DoB = DoB

    def _get_student_info(self):
        return self.__id,self.__name,self.__DoB
    
    def _get_student_id(self):
        return self.__id
    
    def _get_student_name(self):
        return self.__name

def reg_Student_info():
    print("Enter student's info")
    student_id = input("Input student's id: ")
    student_name = input("Input student's name: ")
    student_DoB = input("Input student's DoB: ")
    new_student = Student(student_id,student_name,student_DoB)
    student_list.append(new_student)
    if os.path.exists("students.txt"):
        with open("students.txt","a") as student:
            student.write("{} | {} | {}".format(student_id,student_name,student_DoB)+ "\n")

def reg_course_info():
    print("Enter course's info")
    course_id = input("Input course's id: ")
    course_name = input("Input course's name: ")
    new_course = Course(course_id,course_name)
    course_list.append(new_course)
    if os.path.exists("courses.txt"):
        with open("courses.txt","a") as course:
            course.write(f"{course_id} | {course_name}"+ "\n")


def reg_mark():
    student_id = input("Input student's ID: ")
    student = None
    for s in student_list:
        if s._get_student_id() == student_id:
            student = s
            break
    if student is None:
        print("Student doesn't exist")
        return

    course_id = input("Input course's ID: ")
    course = None
    for c in course_list:
        if c._get_course_id() == course_id:
            course = c
            break
    if course is None:
        print("Course doesn't exist")
        return

    mark = input(f"Enter marks for {student._get_student_name()} in {course._get_course_name()}: ")
    marks[(student_id, course_id)] = mark
    if os.path.exists("marks.txt"):
        with open("marks.txt","a") as marking:
            marking.write(f"{student_id} in {course_id} scored: {mark}"+ "\n")
    

def list_all_students():
    print("Here are all the students: ")
    for i in student_list:
        if isinstance(i,Student):
            print(i._get_student_info())
    print("In the files:")
    if os.path.exists("students.txt"):
        with open("students.txt") as student:
            for s in student:
                print(s)
        
def list_all_courses():
    print("Here are the currently available courses: ")
    for i in course_list:
        if isinstance(i,Course):
            print(i._get_course_info())
    print("In the file:")
    if os.path.exists("courses.txt"):
        with open("courses.txt") as course:
            for c in course:
                print(c)

def list_all_marks():
    for i in marks:
        print(f"{i} : {marks[i]}")
    print("In the file: ")
    if os.path.exists("marks.txt"):
        with open("marks.txt") as mark:
            for m in mark:
                print(m)

def main():
    no_student = int(input("Enter number of students in a class: "))
    no_courses = int(input("Enter number of courses: "))

    for x in range(no_student):
        reg_Student_info()
    for y in range(no_courses):
        reg_course_info()

    print()
    time.sleep(.5)
    list_all_students()
    list_all_courses()
    print()
    time.sleep(.5)

    reg_mark()

    list_all_marks()
    
main()   