class CartItem:
    def __init__(self, member_id, book_no, quantity):
        self.member_id = member_id
        self.book_no = str(book_no)
        self.quantity = int(quantity)

    def __str__(self):
        return f'[{self.book_no}, {self.quantity} (권)]'
