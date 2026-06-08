class Member:
    def __init__(self, id, pw, name):
        self.__member_no = 0
        self.__id = id
        self.__pw = pw
        self.__name = name

    def get_member_no(self):
        return self.__member_no
    def get_id(self):
        return self.__id
    def get_pw(self):
        return self.__pw
    def get_name(self):
        return self.__name
    def set_id(self, id):
        self.__id = id
    def set_pw(self, pw):
        self.__pw = pw
    
    def __str__(self):
        return f'{self.__member_no}\t{self.__id}\t{self.__name}\t{self.__pw}'