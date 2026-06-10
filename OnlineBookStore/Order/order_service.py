from Order.order import Order

class OrderService:
    def __init__(self, order_dao, book_service, cart_service):
        self.dao = order_dao
        self.book_service = book_service
        self.cart_service = cart_service

    def order_book(self, member_id, book_no, quantity):
        book = self.book_service.get_book(book_no)
        quantity = int(quantity)
        if not book:
            return False
        if quantity <= 0 or quantity > 11:
            raise ValueError('주문 수량은 1권 이상 11권 이하여야 합니다')
        book.decrease_stock(quantity)
        total_price = book.get_price() * quantity
        items = [(book.get_book_no(), book.get_title(), quantity, book.get_price())]
        order = Order(self.dao.make_order_no(), member_id, items, total_price)
        return self.dao.insert_order(order)

    def order_cart(self, member_id):
        cart_items = self.cart_service.get_cart(member_id)
        if not cart_items:
            return False

        items = []
        total_price = 0
        for cart_item in cart_items:
            book = self.book_service.get_book(cart_item.book_no)
            if not book:
                raise ValueError(f'{cart_item.book_no} 도서가 존재하지 않습니다')
            if book.get_stock() < cart_item.quantity:
                raise ValueError(f'{book.get_title()} 재고가 부족합니다')

        for cart_item in cart_items:
            book = self.book_service.get_book(cart_item.book_no)
            book.decrease_stock(cart_item.quantity)
            total_price += book.get_price() * cart_item.quantity
            items.append((book.get_book_no(), book.get_title(), cart_item.quantity, book.get_price()))

        order = Order(self.dao.make_order_no(), member_id, items, total_price)
        self.dao.insert_order(order)
        self.cart_service.clear_cart(member_id)
        return True

    def get_member_orders(self, member_id):
        return self.dao.select_orders_by_member_id(member_id)

    def get_all_orders(self):
        return self.dao.select_all_orders()
