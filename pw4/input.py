import os
import math
import numpy as np

import time

student_arr = np.array([])
course_arr = np.array([])
mark_arr = np.array([])

import domains.Course_Class
import domains.Student_Class

def get_no_student():
    no_student = int(input("Enter number of students in a class: "))
    return no_student
    
def get_no_course():
    no_courses = int(input("Enter number of courses: "))
    return no_courses

def reg_student_info():
    print("Enter student's info")
    student_id = input("Input student's id: ")
    student_name = input("Input student's name: ")
    student_DoB = input("Input student's DoB: ")
    new_student = domains.Student_Class.Student(student_id,student_name,student_DoB)
    #student_list.append(new_student)
    np.append(student_arr,new_student)
    if os.path.exists("students.txt"):
        with open("students.txt","a") as student:
            student.write("{} | {} | {}".format(student_id,student_name,student_DoB)+ "\n")

def reg_course_info():
    print("Enter course's info")
    course_id = input("Input course's id: ")
    course_name = input("Input course's name: ")
    course_ects = int(input("Input course's ECTS: "))
    new_course = domains.Course_Class.Course(course_id,course_name,course_ects)
    #course_list.append(new_course)
    np.append(course_arr,new_course)
    if os.path.exists("courses.txt"):
        with open("courses.txt","a") as course:
            course.write(f"{course_id} | {course_name}"+ "\n")

def student_mark_floor(mark): #self made floor to floor decimal without round()
    mark = mark*10
    mark = math.floor(mark)
    mark = mark/10
    return mark

def reg_mark():
    student_id = input("Input student's ID: ")
    student = None
    for s in student_arr:
        if s._get_student_id() == student_id:
            student = s
            break
    if student is None:
        print("Student doesn't exist")
        return

    course_id = input("Input course's ID: ")
    course = None
    for c in course_arr:
        if c._get_course_id() == course_id:
            course = c
            break
    if course is None:
        print("Course doesn't exist")
        return

    mark = float(input(f"Enter marks for {student._get_student_name()} in {course._get_course_name()}: "))
    mark = student_mark_floor(mark)

    np.insert(mark_arr,(student_id, course_id),mark)
    if os.path.exists("marks.txt"):
        with open("marks.txt","a") as marking:
            marking.write(f"{student_id} in {course_id} scored: {mark}"+ "\n")
            
def CalculateGPA():
    student_id = input("Input student's ID: ")
    student = None
    for s in student_arr:
        if s._get_student_id() == student_id:
            student = s
            break
    if student is None:
        print("Student doesn't exist")
        return
    
    total_ects = 0
    total_mark = 0
    for m_idx, m in np.ndenumerate(mark_arr):
        if tuple(m_idx).index(0) == student_id:
            total_mark += m
            for c in course_arr:
                if c._get_course_id() == tuple(m_idx).index(1):
                    total_ects += c._get_course_ects()
            break
    
def End():
    print("Quitting")
    time.sleep(.5)
    print(".")
    time.sleep(.25)
    print("...")
    time.sleep(.35)
    print(".......")
    quit()