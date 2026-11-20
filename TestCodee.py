class Book:
    def __init__(self,title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        is_borrowed = False
    def borrow(self, is_borrowed):
        if is_borrowed == False:
            is_borrowed = True
        else:
            print("Book is already borrowed")
    def return_book(self, is_borrowed):
        if is_borrowed == True:
            is_borrowed = False
            print("Thanks for returning the book")
        else:
            print("Book is not borrowed yet")

book1 = Book("Book1","Author1", True)
book1.borrow(True)
book1.return_book(True)

book2 = Book("Book2","Author2", False)
book2.borrow(False)
book2.return_book(False)

book3 = Book("Book3","Author3", False)
book3.borrow(False)
book3.return_book(False)
