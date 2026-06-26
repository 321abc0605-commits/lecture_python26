from Cart.cart_item import CartItem

class CartService:
    def __init__(self, cart_dao, gifticon_service):
        self.dao = cart_dao
        self.gifticon_service = gifticon_service

    def add_to_cart(self, member_id, gifticon_no, quantity):
        gifticon = self.gifticon_service.get_gifticon(gifticon_no)
        quantity = int(quantity)
        if not gifticon:
            return False
        if quantity <= 0 or quantity > 11:
            raise ValueError('주문 수량은 1개 이상 11개 이하여야 합니다')
        if gifticon.get_stock() < quantity:
            raise ValueError('재고가 부족합니다')
        return self.dao.insert_or_update_item(CartItem(member_id, gifticon_no, quantity))

    def get_cart(self, member_id):
        return self.dao.select_cart(member_id)

    def delete_cart_item(self, member_id, gifticon_no):
        return self.dao.delete_item(member_id, gifticon_no)

    def clear_cart(self, member_id):
        return self.dao.clear_cart(member_id)
