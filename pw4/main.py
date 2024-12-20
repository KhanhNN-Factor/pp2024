import input as ip
import output as op

action_list = [
    "Input number of students in a class",
    "Input number of courses",
    "Input student's info",
    "Input course's info",
    "Input mark",
    "End"
]
action_result = [
    ip.get_no_student,
    ip.get_no_course,
    ip.reg_student_info,
    ip.reg_course_info,
    ip.reg_mark,
    ip.End
]
def get_Input():
    for i,a in enumerate(action_list):
        print("{}.{}".format(i,a))
    act_input = input("What do you want to do: ")

    while not act_input:
        act_input = input("What do you want to do: ")

    action_index = int(act_input)
    if action_index < len(action_list):
       action_result[action_index]()
    else:
        print("Illegal move")

    get_Input()

get_Input()