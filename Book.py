class Book:
    def __init__(self, title, author, price, ISBN):
        self._title = title
        self._author = author
        self._price = price
        self._ISBN = ISBN

    # Title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    
    # Author
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author
    

    # Price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if(new_price < 0):
            raise ValueError("Price must be a positive value")
        self._price = new_price
        

    # ISBN
    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, new_isbn):
        self._isbn = new_isbn