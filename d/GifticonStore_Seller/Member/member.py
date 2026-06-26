class Member:
    def __init__(self, member_id, password, name, role='customer'):
        self.__member_id = member_id
        self.__password = password
        self.__name = name
        self.__role = role  # customer, seller, admin

    def get_member_id(self):
        return self.__member_id

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def is_customer(self):
        return self.__role == 'customer'

    def is_seller(self):
        return self.__role == 'seller'

    def is_admin(self):
        return self.__role == 'admin'

    def __str__(self):
        role_name = {'customer': '회원', 'seller': '판매자', 'admin': '관리자'}.get(self.__role, self.__role)
        return f'[{self.__member_id}, {self.__password}, {self.__name}, {role_name}]'
