class Book:
    def __init__(self, book_no, title, author, publisher, price, stock):
        self.__book_no = str(book_no)
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__price = int(price)
        self.__stock = int(stock)

    def get_book_no(self):
        return self.__book_no

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = int(price)

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        self.__stock = int(stock)

    def decrease_stock(self, quantity):
        if quantity <= 0:
            raise ValueError('수량은 1권 이상이어야 합니다')
        if self.__stock < quantity:
            raise ValueError('재고가 부족합니다')
        self.__stock -= quantity

    def increase_stock(self, quantity):
        self.__stock += int(quantity)

    def __str__(self):
        return f'[{self.__book_no}, {self.__title}, {self.__author}, {self.__publisher}, {self.__price}, {self.__stock}]'
