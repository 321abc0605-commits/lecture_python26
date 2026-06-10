class Member:
    def __init__(self, member_id, password, name):
        self.__member_id = member_id
        self.__password = password
        self.__name = name

    def get_member_id(self):
        return self.__member_id

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_name(self):
        return self.__name

    def __str__(self):
        return f'[{self.__member_id}, {self.__password}, {self.__name}]'
