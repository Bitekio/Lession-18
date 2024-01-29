"""
hw2
"""


class Book:
    """class book"""
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        """
        Инициализация объекта класса Book.

        :param title: Название книги.
        :param year: Год выпуска книги.
        :param publisher: Издатель книги.
        :param genre: Жанр книги.
        :param author: Автор книги.
        :param price: Цена книги в рублях.
        """
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        """
        Метод для ввода данных о книге с клавиатуры.
        """
        self.title = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        """
        Метод для вывода данных о книге на экран.
        """
        print(f"Название: {self.title}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price} руб.")

    def get_title(self):
        """
        Метод для получения названия книги.
        """
        return self.title

    def get_year(self):
        """
        Метод для получения года выпуска книги.
        """
        return self.year

    def get_publisher(self):
        """
        Метод для получения издателя книги.
        """
        return self.publisher

    def get_genre(self):
        """
        Метод для получения жанра книги.
        """
        return self.genre

    def get_author(self):
        """
        Метод для получения автора книги.
        """
        return self.author

    def get_price(self):
        """
        Метод для получения цены книги.
        """
        return self.price


if __name__ == "__main__":
    book1 = Book()
    book1.input_data()

    print("\nИнформация о книге:")
    book1.display_data()

    print(f"\nНазвание книги: {book1.get_title()}")
    print(f"Год выпуска: {book1.get_year()}")
    print(f"Издатель: {book1.get_publisher()}")
    print(f"Жанр: {book1.get_genre()}")
    print(f"Автор: {book1.get_author()}")
    print(f"Цена: {book1.get_price()} руб.")
