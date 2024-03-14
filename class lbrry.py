books = []
class Library:
    def __init__(self):
        self.Book_ID=""
        self.price=""
        self.title=""
        self.author=""
        self.publisher=""

    def addbook(self):
        self.Book_ID=int(input("enter the book ID"))
        self.price=int(input("enter the price of the book"))
        self.title=input("enter the title of the book")
        self.author=input("enter the name of the author")
        self.publisher=input("enter the name of the publisher")
    def display(self):
        print("Book_ID",self.Book_ID)
        print("price",self.price)
        print("title",self.title)
        print("author",self.author)
        print("publisher",self.publisher)
    def update(self):
        key=int(input("enter the ID of the book you want to update the price"))
        new_price=int(input("enter the updated price"))
        for book in books:
            if book[0]==key:
             book[2]=new_price
while True:
    l1 = Library()
    print("1.addbook")
    print("2.display books")
    print("3.update")
    choice=int(input("enter your choice"))
    if choice==2:
        l1.addbook()
    if choice==2:
        l1.display()
    if choice==3:
        l1.update()

