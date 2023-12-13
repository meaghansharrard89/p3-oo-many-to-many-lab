class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("Invalid name.")

    def contracts(self):
        # return list of related contracts
        return [
            contract for contract in Contract.all_contracts if contract.author == self
        ]

    def books(self):
        # return list of related books using Contract class as intermediary
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # create and return a new Contract object between author/spec book with spec date/royalties
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        # return total amount of royalties that author has earned from all contracts
        total_royalties = sum(contract.royalties for contract in self.contracts())
        return total_royalties


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise Exception("Invalid title")

    def contracts(self):
        # return list contracts related to book
        return [
            contract for contract in Contract.all_contracts if contract.book == self
        ]

    def authors(self):
        # Return list of authors related to the book through contracts
        return [contract.author for contract in self.contracts()]


class Contract(Author):
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    # Author getter/setter
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        # author should be an instance of the Author class
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Invalid author.")

    # Book getter/setter
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        # book should be instance of the Book class
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Invalid book.")

    # Date getter/setter
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        # date should represent when contract was signed
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("Invalid date.")

    # Royalties getter/setter
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        # royalties should be a num that reps percentage of royalties author will receive for book
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("Royalties should be an integer.")

    @classmethod
    def contracts_by_date(cls, date):
        # return all contracts that have the same date as the date passed into the method
        matching_contracts = [
            contract for contract in cls.all_contracts if contract.date == date
        ]
        return sorted(matching_contracts, key=lambda contract: contract.date)

    # ChatGPT told me to add this since the last test wasn't passing:
    def __eq__(self, other):
        if isinstance(other, Contract):
            return (
                self.author == other.author
                and self.book == other.book
                and self.date == other.date
                and self.royalties == other.royalties
            )
        return False
