class Order:
    def __init__(self, order_no, member_id, gifticon_no, seller_id, quantity, total_price):
        self.__order_no = str(order_no)
        self.__member_id = member_id
        self.__gifticon_no = str(gifticon_no)
        self.__seller_id = seller_id
        self.__quantity = int(quantity)
        self.__total_price = int(total_price)

    def get_order_no(self):
        return self.__order_no

    def get_member_id(self):
        return self.__member_id

    def get_gifticon_no(self):
        return self.__gifticon_no

    def get_seller_id(self):
        return self.__seller_id

    def get_total_price(self):
        return self.__total_price

    def __str__(self):
        return f'[주문번호:{self.__order_no}, 구매자:{self.__member_id}, 판매자:{self.__seller_id}, 기프티콘:{self.__gifticon_no}, 수량:{self.__quantity}, 총액:{self.__total_price}원]'
