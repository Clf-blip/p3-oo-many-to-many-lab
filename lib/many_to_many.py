# lib/many_to_many.py

class Book:
    all = []

    def __init__(self, title: str):
        self.title = title       # validated by setter
        Book.all.append(self)

    # ---------- title ----------
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise Exception("title must be non-empty str")
        self._title = value

    # ---------- relationship helpers ----------
    def contracts(self):
        """Return all contracts for this book."""
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        """Return all authors linked to this book via contracts."""
        return [c.author for c in self.contracts()]


class Author:
    all = []

    def __init__(self, name: str):
        self.name = name         # validated by setter
        Author.all.append(self)

    # ---------- name ----------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise Exception("name must be non-empty str")
        self._name = value

    # ---------- relationship helpers ----------
    def contracts(self):
        """Return all contracts for this author."""
        return [c for c in Contract.all if c.author is self]

    def books(self):
        """Return all books linked to this author via contracts."""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract involving this author."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Sum royalties from all of the author's contracts."""
        return sum(c.royalties for c in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # validations via property setters
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # ---------- author ----------
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be Author instance")
        self._author = value

    # ---------- book ----------
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be Book instance")
        self._book = value

    # ---------- date ----------
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise Exception("date must be non-empty str")
        self._date = value

    # ---------- royalties ----------
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be int")
        self._royalties = value

    # ---------- class helpers ----------
    @classmethod
    def contracts_by_date(cls, date):
        """Return contracts with an exact matching date."""
        return [c for c in cls.all if c.date == date]
