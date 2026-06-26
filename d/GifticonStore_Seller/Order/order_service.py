from Order.order import Order

class OrderService:
    def __init__(self, order_dao, gifticon_service, cart_service):
        self.dao = order_dao
        self.gifticon_service = gifticon_service
        self.cart_service = cart_service

    def order_gifticon(self, member_id, gifticon_no, quantity):
        gifticon = self.gifticon_service.get_gifticon(gifticon_no)
        quantity = int(quantity)
        if not gifticon:
            return False
        if quantity <= 0 or quantity > 11:
            raise ValueError('주문 수량은 1개 이상 11개 이하여야 합니다')
        gifticon.decrease_stock(quantity)
        total_price = gifticon.get_price() * quantity
        order = Order(self.dao.next_no(), member_id, gifticon_no, gifticon.get_seller_id(), quantity, total_price)
        return self.dao.insert_order(order)

    def order_cart(self, member_id):
        cart = self.cart_service.get_cart(member_id)
        if not cart:
            return False
        for item in cart:
            self.order_gifticon(member_id, item.gifticon_no, item.quantity)
        self.cart_service.clear_cart(member_id)
        return True

    def get_member_orders(self, member_id):
        return self.dao.select_orders_by_member(member_id)

    def get_seller_orders(self, seller_id):
        return self.dao.select_orders_by_seller(seller_id)

    def get_all_orders(self):
        return self.dao.select_all_orders()
