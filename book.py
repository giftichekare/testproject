class Books():
    def __init__(self, book):
        self.book = book
    def get_book(self):
        print(self.book)

my_book = Books("Bible, Project Mnagement, Business Analysis, ITSM, and Pyschology")
my_book.get_book()
