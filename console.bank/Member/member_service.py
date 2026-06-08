from Member.member_dao import MemberDAO
from Member.member import Member

#==================
# 회원 관리 서비스 로직 (Controller) : MemberService
class MemberService:
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '1234'

    def __init__(self, memberDao):
        self.__dao = memberDao
        self.join(Member(MemberService.ADMIN_ID, MemberService.ADMIN_PASSWORD, '관리자'))
        self.current_user = None

    def join(self, member):
        if self.__dao.is_exist(member.get_id()):
            return False
        self.__dao.insert_member(member)
        return True

    def login(self, id, pw):
        member = self.__dao.get_member_info(id)
        if member:
            if pw == member.get_pw():
                self.current_user = id
                return True
        return False
    
    def list_members(self):
        return self.__dao.get_all_members()
    
    def logout(self):
        self.current_user = None

    def view_member_info(self, id):
        return self.__dao.get_member_info(id)

    def update_member_info(self, id, member):
        return self.__dao.update_member_info(id, member)
    
    def update_member_pw(self, id, org_pw, new_pw):
        if self.current_user != id: return False
        member = self.__dao.get_member_info(id)
        if not member: return False
        if member.get_pw() == org_pw:
            member.set_pw(new_pw)
            return True
        return False
    
    def remove_member(self, id):
        print(self.current_user)
        if self.current_user == id or self.current_user == MemberService.ADMIN_ID:
            return self.__dao.remove_member(id)
        return False

if __name__ == '__main__':
    ms = MemberService(MemberDAO())
    ms.join(Member('soonbeom', '1234', '권순범'))
    ms.join(Member('soonsoon', '1111', '순순'))
    members = ms.list_members()
    for member in members:
        print(member)
    ms.login('curi', '1111')
    print(ms.current_user)
    ms.logout()
    print(ms.current_user)
    print(ms.view_member_info('Jae'))
    ms.login(MemberService.ADMIN_ID, MemberService.ADMIN_PASSWORD)
    print(ms.update_member_pw('WonJae', '1234', '4321'))
    print(ms.view_member_info('WonJae'))
    print(ms.remove_member('WonJae'))
    print(ms.view_member_info('WonJae'))