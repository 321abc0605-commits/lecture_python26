from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Book.book_dao import BookDAO
from Book.book_service import BookService
from Cart.cart_dao import CartDAO
from Cart.cart_service import CartService
from Order.order_dao import OrderDAO
from Order.order_service import OrderService

class ConsoleBookStore:
    start_menu = ['종료', '로그인', '회원가입']
    member_menu = ['로그아웃', '도서 목록', '도서 주문', '장바구니 도서 담기', '장바구니 보기', '주문 목록', '내 정보']
    cart_menu = ['돌아가기', '도서 주문', '도서 삭제', '장바구니 비우기']
    myinfo_menu = ['돌아가기', '내정보보기', '비밀번호수정', '회원탈퇴']
    admin_menu = ['로그아웃', '도서 목록', '도서 등록', '도서 정보 수정', '도서 삭제', '회원 목록', '주문 목록']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.bsv = BookService(BookDAO())
        self.csv = CartService(CartDAO(), self.bsv)
        self.osv = OrderService(OrderDAO(), self.bsv, self.csv)

    def main(self):
        self.show_welcome()
        while True:
            result = self.run_start_menu()
            if result == 0:
                break
        self.say_goodbye()

    def show_welcome(self):
        print('================ Jae OnlineBookStore ================')

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

    # 시작 메뉴 ---------------------------------------------------------------
    def run_start_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookStore.start_menu)
            if menu == 0:
                return 0
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_join()

    def menu_login(self):
        member_id = input('아이디 : ')
        password = input('비밀번호 : ')
        print()
        if self.msv.login(member_id, password):
            if self.msv.current_user == MemberService.ADMIN_ID:
                print('관리자 모드로 변경합니다.')
                self.run_admin_menu()
            else:
                print(f'{member_id}님 로그인되었습니다.')
                self.run_member_menu()
        else:
            print('ERROR : 아이디 또는 비밀번호가 잘못되었습니다')

    def menu_join(self):
        member_id = input('생성할 아이디 : ')
        password = input('사용할 비밀번호 : ')
        name = input('이름 : ')
        print()
        member = Member(member_id, password, name)
        if self.msv.join(member):
            print(f'{name}님 회원가입 되었습니다')
        else:
            print('ERROR : 이미 가입된 회원입니다')

    # 회원 메뉴 ---------------------------------------------------------------
    def run_member_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookStore.member_menu)
            if menu == 0:
                self.msv.logout()
                print('로그아웃되었습니다')
                return
            elif menu == 1:
                self.menu_list_books()
            elif menu == 2:
                self.menu_order_book()
            elif menu == 3:
                self.menu_add_cart()
            elif menu == 4:
                self.run_cart_menu()
            elif menu == 5:
                self.menu_list_my_orders()
            elif menu == 6:
                self.run_myinfo_menu()

    def menu_list_books(self):
        print('*** 도서 목록 ***')
        print('--------------------------------------------------')
        books = self.bsv.get_all_books()
        if books:
            for book in books:
                print(book)
        else:
            print('등록된 도서가 없습니다')
        print('--------------------------------------------------')

    def menu_order_book(self):
        self.menu_list_books()
        book_no = input('>> 도서 번호 : ')
        quantity = self.input_int('>> 주문 수량 (11권 이내) : ')
        if quantity is None:
            return
        try:
            result = self.osv.order_book(self.msv.current_user, book_no, quantity)
            if result:
                print('도서를 주문했습니다.')
            else:
                print('ERROR : 잘못된 도서 번호입니다')
        except ValueError as e:
            print(f'ERROR : {e}')

    def menu_add_cart(self):
        print('*** 장바구니 도서 담기 ***')
        self.menu_list_books()
        book_no = input('>> 도서 번호 : ')
        quantity = self.input_int('>> 주문 수량 (11권 이내) : ')
        if quantity is None:
            return
        try:
            result = self.csv.add_to_cart(self.msv.current_user, book_no, quantity)
            if result:
                print('장바구니에 도서를 담았습니다.')
            else:
                print('ERROR : 잘못된 도서 번호입니다')
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
            menu = self.select_menu(ConsoleBookStore.cart_menu)
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
            result = self.osv.order_cart(self.msv.current_user)
            if result:
                print('장바구니 도서를 주문했습니다.')
            else:
                print('ERROR : 장바구니가 비어 있습니다')
        except ValueError as e:
            print(f'ERROR : {e}')

    def menu_delete_cart_item(self):
        book_no = input('>> 삭제할 도서 번호 : ')
        if self.csv.delete_cart_item(self.msv.current_user, book_no):
            print('장바구니에서 도서를 삭제하였습니다.')
        else:
            print('ERROR : 장바구니에 해당 도서가 없습니다')

    def menu_clear_cart(self):
        check = input('장바구니 도서를 모두 삭제합니다. 실행하려면 y 입력 : ')
        if check.lower() == 'y':
            self.csv.clear_cart(self.msv.current_user)
            print('장바구니 도서를 모두 삭제하였습니다.')
        else:
            print('취소되었습니다')

    # 내 정보 메뉴 ------------------------------------------------------------
    def run_myinfo_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookStore.myinfo_menu)
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

    # 관리자 메뉴 -------------------------------------------------------------
    def run_admin_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookStore.admin_menu)
            if menu == 0:
                self.msv.logout()
                print('로그아웃되었습니다')
                return
            elif menu == 1:
                self.menu_list_books()
            elif menu == 2:
                self.menu_add_book()
            elif menu == 3:
                self.menu_update_book()
            elif menu == 4:
                self.menu_delete_book()
            elif menu == 5:
                self.menu_list_members()
            elif menu == 6:
                self.menu_list_all_orders()

    def menu_add_book(self):
        print('*** 도서 등록 ***')
        title = input('>> 도서명 : ')
        author = input('>> 저자 : ')
        publisher = input('>> 출판사 : ')
        price = self.input_int('>> 가격 : ')
        stock = self.input_int('>> 재고량 : ')
        if price is None or stock is None:
            return
        if self.bsv.add_book(title, author, publisher, price, stock):
            print('도서를 등록하였습니다.')
        else:
            print('ERROR : 도서 등록에 실패했습니다')

    def menu_update_book(self):
        print('*** 도서 정보 수정 ***')
        self.menu_list_books()
        book_no = input('>> 도서 번호 : ')
        print('>> 수정할 정보 선택 (1. 가격, 2. 재고량, 3. 도서명)')
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
        if self.bsv.update_book_info(book_no, select, value):
            print('도서 정보를 수정하였습니다.')
        else:
            print('ERROR : 잘못된 도서 번호입니다')

    def menu_delete_book(self):
        print('*** 도서 삭제 ***')
        self.menu_list_books()
        book_no = input('>> 삭제할 도서 번호 : ')
        if self.bsv.delete_book(book_no):
            print('도서를 삭제하였습니다.')
        else:
            print('ERROR : 잘못된 도서 번호입니다')

    def menu_list_members(self):
        print('*** 회원 목록 ***')
        print('----------------------')
        members = self.msv.list_members()
        if members:
            for member in members:
                print(member)
        else:
            print('가입된 회원이 없습니다')
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
    app = ConsoleBookStore()
    app.main()
