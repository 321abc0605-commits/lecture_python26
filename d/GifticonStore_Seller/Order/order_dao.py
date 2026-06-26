class OrderDAO:
    def __init__(self):
        self.__order_db = {}
        self.__sequence = 1000

    def next_no(self):
        self.__sequence += 1
        return str(self.__sequence)

    def insert_order(self, order):
        self.__order_db[order.get_order_no()] = order
        return True

    def select_orders_by_member(self, member_id):
        orders = [o for o in self.__order_db.values() if o.get_member_id() == member_id]
        return orders if orders else None

    def select_orders_by_seller(self, seller_id):
        orders = [o for o in self.__order_db.values() if o.get_seller_id() == seller_id]
        return orders if orders else None

    def select_all_orders(self):
        orders = list(self.__order_db.values())
        return orders if orders else None
