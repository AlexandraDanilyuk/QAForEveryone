class Books:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def this_book(self):
        return (f'Is author {self.author} and title {self.title}')

book1 = Books(author='Tom Mann', title='Mor')
print(book1.this_book())

class Fiction(Books):
    def __init__(self, author, title, tip):
        super().__init__(author, title)
        self.tip = tip

    def book_info(self):
        print(f'This book author {self.author} - {self.title} and it is {self.tip}')

book2 = Fiction('Todd Dude', 'Goverment', 'roman')
book2.book_info()

class Nonfiction(Books):
    def __init__(self, author, title, tip, theme):
        super().__init__(author, title)
        self.tip = tip
        self.__theme = theme

    def book_info(self):
        print(f'This book {self.author} {self.title} and {self.__theme} {self.tip}')

book3 = Nonfiction('Ada Lovely', 'Birds', 'novell', 'sciense')
book3.book_info()
