class Student:
    def __init__(self,id,name,DoB):
        self.__id = id
        self.__name = name
        self.__DoB = DoB
        self.__GPA = 0.0

    def _get_student_info(self):
        return self.__id,self.__name,self.__DoB
    
    def _get_student_id(self):
        return self.__id
    
    def _get_student_name(self):
        return self.__name