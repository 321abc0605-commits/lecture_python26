from Book.book import Book

class BookDAO:
    def __init__(self):
        self.__book_db = {}
        self.__next_book_no = 116
        self.insert_book(Book('001', '죄와 벌', '표도르 도스토옙스키', '민음사', 11000, 10))
        self.insert_book(Book('002', '체스 이야기', '슈테판 츠바이크', '세창출판사', 8000, 15))
        self.insert_book(Book('003', '구덩이', '루이스 새커', '창비', 15000, 15))
        self.insert_book(Book('004', '신과 함께', '주호민', '문학동네', 13000, 8))
        self.insert_book(Book('005', '노 게임 노 라이프', '카미야 유우', '데이트 엔터', 6000, 4))
        self.insert_book(Book('006', '싯다르타', '헤르만 헤세', '민음사', 8000, 5))
        self.insert_book(Book('007', '화산귀환', '비가', '러프미디어', 14000, 4))


    def make_book_no(self):
        book_no = str(self.__next_book_no)
        self.__next_book_no += 1
        return book_no

    def insert_book(self, book):
        book_no = book.get_book_no()
        if book_no in self.__book_db:
            return False
        self.__book_db[book_no] = book
        return True

    def select_book_by_no(self, book_no):
        return self.__book_db.get(str(book_no))

    def select_all_books(self):
        books = list(self.__book_db.values())
        return books if books else None

    def update_book(self, book_no, book):
        book_no = str(book_no)
        if book_no not in self.__book_db:
            return False
        self.__book_db[book_no] = book
        return True

    def delete_book(self, book_no):
        book_no = str(book_no)
        if book_no not in self.__book_db:
            return False
        del self.__book_db[book_no]
        return True
