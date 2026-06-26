class CartItem:
    def __init__(self, member_id, gifticon_no, quantity):
        self.member_id = member_id
        self.gifticon_no = str(gifticon_no)
        self.quantity = int(quantity)

    def __str__(self):
        return f'[{self.gifticon_no}, {self.quantity}개]'
