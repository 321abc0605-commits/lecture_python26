from Member.member import Member

class MemberDAO:
    def __init__(self):
        self.__member_db = {}
        self.insert_member(Member('admin', '1111', '관리자'))
        self.insert_member(Member('test', '1111', '고재혁'))

    def insert_member(self, member):
        member_id = member.get_member_id()
        if member_id in self.__member_db:
            return False
        self.__member_db[member_id] = member
        return True

    def select_member_by_id(self, member_id):
        return self.__member_db.get(member_id)

    def select_all_members(self):
        members = list(self.__member_db.values())
        return members if members else None

    def update_member(self, member_id, member):
        if member_id not in self.__member_db:
            return False
        self.__member_db[member_id] = member
        return True

    def delete_member(self, member_id):
        if member_id not in self.__member_db:
            return False
        del self.__member_db[member_id]
        return True
