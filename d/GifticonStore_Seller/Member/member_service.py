class MemberService:
    def __init__(self, member_dao):
        self.dao = member_dao
        self.current_user = None

    def join(self, member):
        return self.dao.insert_member(member)

    def login(self, member_id, password):
        member = self.dao.select_member_by_id(member_id)
        if member and member.get_password() == password:
            self.current_user = member_id
            return True
        return False

    def logout(self):
        self.current_user = None

    def get_current_member(self):
        if not self.current_user:
            return None
        return self.dao.select_member_by_id(self.current_user)

    def get_current_role(self):
        member = self.get_current_member()
        return member.get_role() if member else None

    def view_member_info(self, member_id):
        return self.dao.select_member_by_id(member_id)

    def update_member_pw(self, member_id, old_pw, new_pw):
        member = self.dao.select_member_by_id(member_id)
        if not member or member.get_password() != old_pw:
            return False
        member.set_password(new_pw)
        return self.dao.update_member(member_id, member)

    def remove_member(self, member_id, password=None):
        member = self.dao.select_member_by_id(member_id)
        if not member:
            return False
        if password is not None and member.get_password() != password:
            return False
        return self.dao.delete_member(member_id)

    def list_members(self):
        return self.dao.select_all_members()

    def list_customers(self):
        return self.dao.select_members_by_role('customer')

    def list_sellers(self):
        return self.dao.select_members_by_role('seller')
