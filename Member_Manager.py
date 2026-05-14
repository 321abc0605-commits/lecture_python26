class Member:
    def __init__(self, num, userid, password, name, phone, address):
        self.num = num
        self.userid = userid
        self.password = password
        self.name = name
        self.phone = phone
        self.address = address


class MemberService:
    def __init__(self):
        self.member_list = []

    def add_member(self):
        num = len(self.member_list) + 1

        userid = input("아이디: ")
        password = input("비밀번호: ")
        name = input("이름: ")
        phone = input("전화번호: ")
        address = input("주소: ")

        member = Member(num, userid, password, name, phone, address)

        self.member_list.append(member)

        print("회원가입 완료")

    def list_member(self):
        for member in self.member_list:
            print(member.num, member.userid, member.name)

    def detail_member(self):
        userid = input("조회할 아이디: ")

        for member in self.member_list:
            if member.userid == userid:
                print("회원번호:", member.num)
                print("이름:", member.name)
                print("전화번호:", member.phone)
                print("주소:", member.address)
                return

        print("회원이 없습니다.")

    def update_member(self):
        userid = input("수정할 아이디: ")

        for member in self.member_list:
            if member.userid == userid:
                member.phone = input("새 전화번호: ")
                member.address = input("새 주소: ")

                print("수정 완료")
                return

        print("회원이 없습니다.")

    def delete_member(self):
        userid = input("삭제할 아이디: ")

        for member in self.member_list:
            if member.userid == userid:
                self.member_list.remove(member)

                print("삭제 완료")
                return

        print("회원이 없습니다.")


def main():
    service = MemberService()

    while True:
        print("\n===== 회원 관리 =====")
        print("1. 회원가입")
        print("2. 회원목록")
        print("3. 회원상세정보")
        print("4. 회원정보수정")
        print("5. 회원탈퇴")
        print("0. 종료")

        menu = input("메뉴 선택: ")

        if menu == "1":
            service.add_member()

        elif menu == "2":
            service.list_member()

        elif menu == "3":
            service.detail_member()

        elif menu == "4":
            service.update_member()

        elif menu == "5":
            service.delete_member()

        elif menu == "0":
            print("프로그램 종료")
            break

        else:
            print("잘못된 입력")


main()