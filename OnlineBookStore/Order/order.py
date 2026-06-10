from datetime import datetime

class Order:
    def __init__(self, order_no, member_id, items, total_price, address='서울시 송파구(010)'):
        self.order_no = order_no
        self.member_id = member_id
        self.items = items  # [(book_no, title, quantity, price)]
        self.total_price = int(total_price)
        self.address = address
        self.order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        item_text = ', '.join([f'{book_no} {title} {qty}권' for book_no, title, qty, price in self.items])
        return f'[{self.order_no}, {self.member_id}, {self.order_date}, {self.total_price}원, {self.address}]\n    *** {item_text}'
