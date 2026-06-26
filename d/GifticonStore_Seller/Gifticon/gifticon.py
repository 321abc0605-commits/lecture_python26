class Gifticon:
    def __init__(self, gifticon_no, seller_id, name, brand, category, price, stock):
        self.__gifticon_no = str(gifticon_no)
        self.__seller_id = seller_id
        self.__name = name
        self.__brand = brand
        self.__category = category
        self.__price = int(price)
        self.__stock = int(stock)

    def get_gifticon_no(self):
        return self.__gifticon_no

    def get_seller_id(self):
        return self.__seller_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_brand(self):
        return self.__brand

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = int(price)

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        self.__stock = int(stock)

    def decrease_stock(self, quantity):
        quantity = int(quantity)
        if self.__stock < quantity:
            raise ValueError('재고가 부족합니다')
        self.__stock -= quantity

    def __str__(self):
        return f'[{self.__gifticon_no}, 판매자:{self.__seller_id}, {self.__name}, {self.__brand}, {self.__category}, {self.__price}원, 재고 {self.__stock}개]'
