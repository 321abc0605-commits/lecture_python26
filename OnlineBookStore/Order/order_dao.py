class OrderDAO:
    def __init__(self):
        self.__order_db = {}
        self.__next_order_no = 1001

    def make_order_no(self):
        order_no = str(self.__next_order_no)
        self.__next_order_no += 1
        return order_no

    def insert_order(self, order):
        self.__order_db[order.order_no] = order
        return True

    def select_orders_by_member_id(self, member_id):
        orders = [order for order in self.__order_db.values() if order.member_id == member_id]
        return orders if orders else None

    def select_all_orders(self):
        orders = list(self.__order_db.values())
        return orders if orders else None
