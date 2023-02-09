class Employee:
    def __init__(self, name, id_num, dept, job):
        self.__name = name
        self.__id_num = id_num
        self.__dept = dept
        self.__job = job

    def set_name(self, name):
        self.__name = name

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def set_dept(self, dept):
        self.__dept = dept

    def set_job(self, job):
        self.__job = job

    def get_name(self):
        return self.__name

    def get_id_num(self):
        return self.__id_num

    def get_dept(self, dept):
        return self.__dept

    def get_job(self, job):
        return self.__job

    def __str__(self):
        return self.__name + ', ' + self.__id_num + ', ' + \
            self.__dept + ', ' + self.__job


