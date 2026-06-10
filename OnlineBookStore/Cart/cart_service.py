from Cart.cart_item import CartItem

class CartService:
    def __init__(self, cart_dao, book_service):
        self.dao = cart_dao
        self.book_service = book_service

    def add_to_cart(self, member_id, book_no, quantity):
        book = self.book_service.get_book(book_no)
        quantity = int(quantity)
        if not book:
            return False
        if quantity <= 0 or quantity > 11:
            raise ValueError('주문 수량은 1권 이상 11권 이하여야 합니다')
        if book.get_stock() < quantity:
            raise ValueError('재고가 부족합니다')
        return self.dao.insert_or_update_item(CartItem(member_id, book_no, quantity))

    def get_cart(self, member_id):
        return self.dao.select_cart(member_id)

    def delete_cart_item(self, member_id, book_no):
        return self.dao.delete_item(member_id, book_no)

    def clear_cart(self, member_id):
        return self.dao.clear_cart(member_id)
