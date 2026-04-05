"""Book store.
Klass Book
__init__(self, title: str, author: str, price: float, rating: float) - konstruktor, mis
määrab raamatule tiitli, autori, hinna ja reitingu (hinnangu ehk populaarsuse).

Klass Store
__init__(self, name: str, rating: float) - konstruktor, mis määrab raamatu poele nime ja
minimaalse reitingu (raamatute reitingu) selles poes.

can_add_book(self, book: Book) - meetod, mis kontrollib, kas antud raamatut saab poodi
lisada. Tagastab vastavalt tõeväärtuse. Raamatut saab poodi lisada juhul kui:
sama autori ja tiitliga raamatut ei ole veel antud poes olemas
raamatu oma rating on >= kui poe rating
Meetod tagastab True, kui raamatut saab poodi lisada ja False vastasel juhul.

add_book(self, book: Book) - meetod, mis lisab raamatut poodi kui see on võimalik.

can_remove_book(self, book: Book) - meetod kontrollib, kas antud raamatut saab poest
eemaldada. Eemaldada saab raamatut, mis on antud poes olemas. Tagastab tõeväärtuse
(True, kui raamat on poes, False, kui raamatut pole poes).

remove_book(self, book: Book) - meetod, mis eemaldab raamatu poest, kui see on võimalik.

get_all_books(self) - meetod, mis tagastab listi raamatutega, mis on antud poes olemas.

get_books_by_price(self) - meetod, mis tagastab raamatud sorteeritud hinna alusel
(odavamad enne).

get_most_popular_book(self) - meetod, mis tagastab listi kõige populaarsema (kõrgeima
reitinguga) raamatuga (raamatutega) selles poes. Kui mitu tükki on sama reitinguga, siis
on listis mitu raamatut."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        """
        self.name = name
        self.rating = rating
        self.book_list =

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        if book title == book.title and book author == book.author:
            return False


    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        pass

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        pass

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        pass

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        pass

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        pass

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        pass
