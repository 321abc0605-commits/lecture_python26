class Member:
    def __init__(self, member_no, member_id, pw, name, call_no, address):
        self.__member_no = member_no
        self.__member_id = member_id
        self.__pw = pw
        self.__name = name
        self.__call_no = call_no
        self.__address = address
        
    def __str__(self):
        return f'{self.__member_no}\t{self.__member_id}\t{self.__pw}\t{self.__name}\t{self.__call_no}\t{self.__address}'

    # Getter 메서드
    def get_member_no(self):
        return self.__member_no
    def get_member_id(self):
        return self.__member_id
    def get_pw(self):
        return self.__pw
    def get_name(self):
        return self.__name
    def get_call_no(self):
        return self.__call_no
    def get_address(self):
        return self.__address

    # Setter 메서드
    def set_pw(self, pw):
        self.__pw = pw
    def set_name(self, name):
        self.__name = name
    def set_call_no(self, call_no):
        self.__call_no = call_no
    def set_address(self, address):
        self.__address = address


class MemberService:
    def __init__(self):
        self.__member_list = []

    def member_sign(self, member_no, member_id, pw, name, call_no, address):
        member = Member(member_no, member_id, pw, name, call_no, address)
        self.__member_list.append(member)
        return True
    
    def list_member(self):
        return self.__member_list

    def member_detail(self, member_id):
        for member in self.__member_list:
            if member.get_member_id() == member_id:
                return member
        return None

    def member_edit(self, member_id, new_pw, new_name, new_call_no, new_address):
        member = self.member_detail(member_id)
        if member:
            member.set_pw(new_pw)
            member.set_name(new_name)
            member.set_call_no(new_call_no)
            member.set_address(new_address)
            return True
        return False

    def member_del(self, member_id):
        member = self.member_detail(member_id)
        if member:
            self.__member_list.remove(member)
            return True
        return False


def select_menu():
    print('=====================================================================================')
    print(' 1. 회원가입 | 2. 회원목록 | 3. 회원상세정보 | 4. 회원정보수정 | 5. 회원탈퇴 | 0.종료')
    print('=====================================================================================')

    try:
        menu = int(input('>> 메뉴 선택 : '))
        return menu
    except ValueError:
        return -1


mservice = MemberService()

print()
print(' =========== MEMBER ===========')
while True:
    menu = select_menu()
    if menu == 0: 
        break
        
    elif menu == 1:
        member_no = input("> 회원번호 : ")
        member_id = input("> 아이디 : ")
        pw = input("> 비밀번호 : ")
        name = input("> 이름 : ")
        call_no = input("> 전화번호 : ")
        address = input("> 주소 : ")

        if mservice.member_sign(member_no, member_id, pw, name, call_no, address):
            print('결과 : 회원가입이 완료 되었습니다.')
    
    elif menu == 2:
        print('-------------')
        print(' 회원목록')
        print('-------------')
        
        try:
            member_list = mservice.list_member()
            if not member_list:
                raise ValueError("EmptyMember")
            for member in member_list:
                print(f"- {member.get_member_id()}")
                
        except ValueError:
            print('등록된 회원정보가 없습니다')

    elif menu == 3:
        print('-------------')
        print(' 회원상세정보')
        print('-------------')
        
        try:
            member_id = input('> 조회할 아이디 : ')
            member = mservice.member_detail(member_id)
            if not member:
                raise ValueError("NoMember")
            print(f"회원번호 : {member.get_member_no()}")
            print(f"아이디   : {member.get_member_id()}")
            print(f"비밀번호 : {member.get_pw()}")
            print(f"이름     : {member.get_name()}")
            print(f"전화번호 : {member.get_call_no()}")
            print(f"주소     : {member.get_address()}")
            
        except ValueError:
            print("결과 : 일치하는 회원이 없습니다.")
            
    elif menu == 4:
        print('-------------')
        print(' 회원정보수정')
        print('-------------')
        
        try:
            member_id = input('> 수정할 아이디 : ')
            if not mservice.member_detail(member_id):
                raise ValueError("NoMember")
            new_pw = input("> 새 비밀번호 : ")
            new_name = input("> 새 이름 : ")
            new_call_no = input("> 새 전화번호 : ")
            new_address = input("> 새 주소 : ")
            if mservice.member_edit(member_id, new_pw, new_name, new_call_no, new_address):
                print('결과 : 회원 정보가 수정되었습니다.')
                
        except ValueError:
            print("결과 : 일치하는 회원이 없습니다.")
        
    elif menu == 5:
        print('-------------')
        print(' 회원탈퇴')
        print('-------------')
        try:
            member_id = input('> 탈퇴할 아이디 : ')
            if not mservice.member_del(member_id):
                raise ValueError
            print('결과 : 회원 탈퇴가 완료되었습니다.')

        except ValueError:
            print("결과 : 일치하는 회원이 없습니다.")