from Book.book import Book

class BookService:
    def __init__(self, book_dao):
        self.dao = book_dao

    def get_all_books(self):
        return self.dao.select_all_books()

    def get_book(self, book_no):
        return self.dao.select_book_by_no(book_no)

    def add_book(self, title, author, publisher, price, stock):
        book_no = self.dao.make_book_no()
        book = Book(book_no, title, author, publisher, price, stock)
        return self.dao.insert_book(book)

    def update_book_info(self, book_no, select, value):
        book = self.dao.select_book_by_no(book_no)
        if not book:
            return False
        if select == 1:
            book.set_price(value)
        elif select == 2:
            book.set_stock(value)
        elif select == 3:
            book.set_title(value)
        else:
            return False
        return self.dao.update_book(book_no, book)

    def delete_book(self, book_no):
        return self.dao.delete_book(book_no)
