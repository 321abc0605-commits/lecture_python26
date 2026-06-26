from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Gifticon.gifticon_dao import GifticonDAO
from Gifticon.gifticon_service import GifticonService
from Cart.cart_dao import CartDAO
from Cart.cart_service import CartService
from Order.order_dao import OrderDAO
from Order.order_service import OrderService

class ConsoleGifticonStore:
    start_menu = ['종료', '로그인', '회원가입', '판매자 가입']
    customer_menu = ['로그아웃', '기프티콘 목록', '기프티콘 구매', '장바구니 기프티콘 담기', '장바구니 보기', '주문 목록', '내 정보']
    cart_menu = ['돌아가기', '기프티콘 구매', '기프티콘 삭제', '장바구니 비우기']
    myinfo_menu = ['돌아가기', '내정보보기', '비밀번호수정', '회원탈퇴']
    seller_menu = ['로그아웃', '내 기프티콘 목록', '기프티콘 등록', '기프티콘 정보 수정', '기프티콘 삭제', '판매 내역']
    admin_menu = ['로그아웃', '전체 기프티콘 목록', '회원 목록', '판매자 목록', '전체 주문 목록', '기프티콘 삭제']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.gsv = GifticonService(GifticonDAO())
        self.csv = CartService(CartDAO(), self.gsv)
        self.osv = OrderService(OrderDAO(), self.gsv, self.csv)

    def main(self):
        self.show_welcome()
        while True:
            result = self.run_start_menu()
            if result == 0:
                break
        self.say_goodbye()

    def show_welcome(self):
        print('================ Jae GifticonStore ================')

    def say_goodbye(self):
        print('============ 이용해주셔서 감사합니다 ============')

    def select_menu(self, menu_list):
        print('\n====================== MENU ======================')
        for i in range(1, len(menu_list)):
            print(f'{i}. {menu_list[i]} | ', end='')
        print(f'0. {menu_list[0]}')
        print('==================================================')
        try:
            menu = int(input('>> 메뉴 선택 : '))
            if not (0 <= menu <= len(menu_list) - 1):
                raise ValueError
            print()
            return menu
        except ValueError:
            print('ERROR : 잘못된 입력입니다')
            return -1

    def input_int(self, message):
        try:
            return int(input(message))
        except ValueError:
            print('ERROR : 숫자로 입력해야 합니다')
            return None

    def run_start_menu(self):
        while True:
            menu = self.select_menu(ConsoleGifticonStore.start_menu)
            if menu == 0:
                return 0
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_join_customer()
            elif menu == 3:
                self.menu_join_seller()

    def menu_login(self):
        member_id = input('아이디 : ')
        password = input('비밀번호 : ')
        print()
        if self.msv.login(member_id, password):
            role = self.msv.get_current_role()
            if role == 'admin':
                print('관리자 모드로 변경합니다.')
                self.run_admin_menu()
            elif role == 'seller':
                print(f'{member_id} 판매자님 로그인되었습니다.')
                self.run_seller_menu()
            else:
                print(f'{member_id}님 로그인되었습니다.')
                self.run_customer_menu()
        else:
            print('ERROR : 아이디 또는 비밀번호가 잘못되었습니다')

    def menu_join_customer(self):
        member_id = input('생성할 아이디 : ')
        password = input('사용할 비밀번호 : ')
        name = input('이름 : ')
        print()
        if self.msv.join(Member(member_id, password, name, 'customer')):
            print(f'{name}님 회원가입 되었습니다')
        else:
            print('ERROR : 이미 가입된 회원입니다')

    def menu_join_seller(self):
        member_id = input('생성할 판매자 아이디 : ')
        password = input('사용할 비밀번호 : ')
        name = input('판매자명 : ')
        print()
        if self.msv.join(Member(member_id, password, name, 'seller')):
            print(f'{name}님 판매자 가입 되었습니다')
        else:
            print('ERROR : 이미 가입된 아이디입니다')

    # 회원 메뉴 ---------------------------------------------------------------
    def run_customer_menu(self):
        while True:
            menu = self.select_menu(ConsoleGifticonStore.customer_menu)
            if menu == 0:
                self.msv.logout()
                print('로그아웃되었습니다')
                return
            elif menu == 1:
                self.menu_list_gifticons()
            elif menu == 2:
                self.menu_order_gifticon()
            elif menu == 3:
                self.menu_add_cart()
            elif menu == 4:
                self.run_cart_menu()
            elif menu == 5:
                self.menu_list_my_orders()
            elif menu == 6:
                self.run_myinfo_menu()

    def menu_list_gifticons(self):
        print('*** 기프티콘 목록 ***')
        print('--------------------------------------------------')
        gifticons = self.gsv.get_all_gifticons()
        if gifticons:
            for gifticon in gifticons:
                print(gifticon)
        else:
            print('등록된 기프티콘이 없습니다')
        print('--------------------------------------------------')

    def menu_order_gifticon(self):
        self.menu_list_gifticons()
        gifticon_no = input('>> 기프티콘 번호 : ')
        quantity = self.input_int('>> 주문 수량 (11개 이내) : ')
        if quantity is None:
            return
        try:
            if self.osv.order_gifticon(self.msv.current_user, gifticon_no, quantity):
                print('기프티콘을 구매했습니다.')
            else:
                print('ERROR : 잘못된 기프티콘 번호입니다')
        except ValueError as e:
            print(f'ERROR : {e}')

    def menu_add_cart(self):
        print('*** 장바구니 기프티콘 담기 ***')
        self.menu_list_gifticons()
        gifticon_no = input('>> 기프티콘 번호 : ')
        quantity = self.input_int('>> 주문 수량 (11개 이내) : ')
        if quantity is None:
            return
        try:
            if self.csv.add_to_cart(self.msv.current_user, gifticon_no, quantity):
                print('장바구니에 기프티콘을 담았습니다.')
            else:
                print('ERROR : 잘못된 기프티콘 번호입니다')
        except ValueError as e:
            print(f'ERROR : {e}')

    def menu_list_my_orders(self):
        print('*** 주문 목록 ***')
        print('--------------------------------------------------')
        orders = self.osv.get_member_orders(self.msv.current_user)
        if orders:
            for order in orders:
                print(order)
        else:
            print('주문 내역이 없습니다')
        print('--------------------------------------------------')

    # 장바구니 메뉴 -----------------------------------------------------------
    def run_cart_menu(self):
        while True:
            self.menu_show_cart()
            menu = self.select_menu(ConsoleGifticonStore.cart_menu)
            if menu == 0:
                return
            elif menu == 1:
                self.menu_order_cart()
            elif menu == 2:
                self.menu_delete_cart_item()
            elif menu == 3:
                self.menu_clear_cart()

    def menu_show_cart(self):
        print('*** 장바구니 보기 ***')
        print('----------------------')
        cart = self.csv.get_cart(self.msv.current_user)
        if cart:
            for item in cart:
                print(item)
        else:
            print('장바구니가 비어 있습니다')
        print('----------------------')

    def menu_order_cart(self):
        try:
            if self.osv.order_cart(self.msv.current_user):
                print('장바구니 기프티콘을 구매했습니다.')
            else:
                print('ERROR : 장바구니가 비어 있습니다')
        except ValueError as e:
            print(f'ERROR : {e}')

    def menu_delete_cart_item(self):
        gifticon_no = input('>> 삭제할 기프티콘 번호 : ')
        if self.csv.delete_cart_item(self.msv.current_user, gifticon_no):
            print('장바구니에서 기프티콘을 삭제하였습니다.')
        else:
            print('ERROR : 장바구니에 해당 기프티콘이 없습니다')

    def menu_clear_cart(self):
        check = input('장바구니 기프티콘을 모두 삭제합니다. 실행하려면 y 입력 : ')
        if check.lower() == 'y':
            self.csv.clear_cart(self.msv.current_user)
            print('장바구니 기프티콘을 모두 삭제하였습니다.')
        else:
            print('취소되었습니다')

    # 내 정보 메뉴 ------------------------------------------------------------
    def run_myinfo_menu(self):
        while True:
            menu = self.select_menu(ConsoleGifticonStore.myinfo_menu)
            if menu == 0:
                return
            elif menu == 1:
                print(self.msv.view_member_info(self.msv.current_user))
            elif menu == 2:
                self.menu_update_pw()
            elif menu == 3:
                self.menu_delete_membership()
                return

    def menu_update_pw(self):
        old_pw = input('현재 비밀번호 : ')
        new_pw = input('새 비밀번호 : ')
        if self.msv.update_member_pw(self.msv.current_user, old_pw, new_pw):
            print('비밀번호가 바뀌었습니다')
        else:
            print('ERROR : 비밀번호가 일치하지 않습니다')

    def menu_delete_membership(self):
        password = input('비밀번호 확인 : ')
        if self.msv.remove_member(self.msv.current_user, password):
            print('계정이 삭제되었습니다')
            self.msv.logout()
        else:
            print('ERROR : 비밀번호가 일치하지 않습니다')

    # 판매자 메뉴 -------------------------------------------------------------
    def run_seller_menu(self):
        while True:
            menu = self.select_menu(ConsoleGifticonStore.seller_menu)
            if menu == 0:
                self.msv.logout()
                print('로그아웃되었습니다')
                return
            elif menu == 1:
                self.menu_list_my_gifticons()
            elif menu == 2:
                self.menu_add_gifticon()
            elif menu == 3:
                self.menu_update_gifticon()
            elif menu == 4:
                self.menu_delete_gifticon()
            elif menu == 5:
                self.menu_list_seller_orders()

    def menu_list_my_gifticons(self):
        print('*** 내 기프티콘 목록 ***')
        print('--------------------------------------------------')
        gifticons = self.gsv.get_seller_gifticons(self.msv.current_user)
        if gifticons:
            for gifticon in gifticons:
                print(gifticon)
        else:
            print('등록한 기프티콘이 없습니다')
        print('--------------------------------------------------')

    def menu_add_gifticon(self):
        print('*** 기프티콘 등록 ***')
        name = input('>> 상품명 : ')
        brand = input('>> 브랜드 : ')
        category = input('>> 분류 : ')
        price = self.input_int('>> 가격 : ')
        stock = self.input_int('>> 재고량 : ')
        if price is None or stock is None:
            return
        try:
            if self.gsv.add_gifticon(self.msv.current_user, name, brand, category, price, stock):
                print('기프티콘을 등록하였습니다.')
            else:
                print('ERROR : 기프티콘 등록에 실패했습니다')
        except ValueError as e:
            print(f'ERROR : {e}')

    def menu_update_gifticon(self):
        print('*** 기프티콘 정보 수정 ***')
        if self.msv.get_current_role() == 'seller':
            self.menu_list_my_gifticons()
        else:
            self.menu_list_gifticons()
        gifticon_no = input('>> 기프티콘 번호 : ')
        print('>> 수정할 정보 선택 (1. 가격, 2. 재고량, 3. 상품명)')
        select = self.input_int('>> 선택 : ')
        if select is None:
            return
        if select in [1, 2]:
            value = self.input_int('>> 수정 값 : ')
            if value is None:
                return
        elif select == 3:
            value = input('>> 수정 값 : ')
        else:
            print('ERROR : 잘못된 선택입니다')
            return
        try:
            if self.gsv.update_gifticon_info(gifticon_no, self.msv.current_user, select, value):
                print('기프티콘 정보를 수정하였습니다.')
            else:
                print('ERROR : 잘못된 기프티콘 번호입니다')
        except PermissionError as e:
            print(f'ERROR : {e}')

    def menu_delete_gifticon(self):
        print('*** 기프티콘 삭제 ***')
        if self.msv.get_current_role() == 'seller':
            self.menu_list_my_gifticons()
        else:
            self.menu_list_gifticons()
        gifticon_no = input('>> 삭제할 기프티콘 번호 : ')
        try:
            if self.gsv.delete_gifticon(gifticon_no, self.msv.current_user):
                print('기프티콘을 삭제하였습니다.')
            else:
                print('ERROR : 잘못된 기프티콘 번호입니다')
        except PermissionError as e:
            print(f'ERROR : {e}')

    def menu_list_seller_orders(self):
        print('*** 판매 내역 ***')
        print('--------------------------------------------------')
        orders = self.osv.get_seller_orders(self.msv.current_user)
        if orders:
            for order in orders:
                print(order)
        else:
            print('판매 내역이 없습니다')
        print('--------------------------------------------------')

    # 관리자 메뉴 -------------------------------------------------------------
    def run_admin_menu(self):
        while True:
            menu = self.select_menu(ConsoleGifticonStore.admin_menu)
            if menu == 0:
                self.msv.logout()
                print('로그아웃되었습니다')
                return
            elif menu == 1:
                self.menu_list_gifticons()
            elif menu == 2:
                self.menu_list_customers()
            elif menu == 3:
                self.menu_list_sellers()
            elif menu == 4:
                self.menu_list_all_orders()
            elif menu == 5:
                self.menu_delete_gifticon()

    def menu_list_customers(self):
        print('*** 회원 목록 ***')
        print('----------------------')
        members = self.msv.list_customers()
        if members:
            for member in members:
                print(member)
        else:
            print('가입된 회원이 없습니다')
        print('----------------------')

    def menu_list_sellers(self):
        print('*** 판매자 목록 ***')
        print('----------------------')
        sellers = self.msv.list_sellers()
        if sellers:
            for seller in sellers:
                print(seller)
        else:
            print('가입된 판매자가 없습니다')
        print('----------------------')

    def menu_list_all_orders(self):
        print('*** 전체 주문 목록 ***')
        print('--------------------------------------------------')
        orders = self.osv.get_all_orders()
        if orders:
            for order in orders:
                print(order)
        else:
            print('주문 내역이 없습니다')
        print('--------------------------------------------------')

if __name__ == '__main__':
    app = ConsoleGifticonStore()
    app.main()
