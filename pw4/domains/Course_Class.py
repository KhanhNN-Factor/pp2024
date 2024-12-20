class Course:
    def __init__(self,id,name,ects):
        self.__id = id
        self.__name = name
        self.__ects = ects

    def _get_course_info(self):
        return self.__id,self.__name
    
    def _get_course_id(self):
        return self.__id
    
    def _get_course_name(self):
        return self.__name
    
    def _get_course_ects(self):
        return self.__ects
