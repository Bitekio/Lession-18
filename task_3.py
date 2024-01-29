"""
hw3
"""


class Stadium:
    """class stadium"""
    def __init__(self, name="", opening_date="", country="", city="", capacity=0):
        """
        Инициализация объекта класса Stadium.

        :param name: Название стадиона.
        :param opening_date: Дата открытия стадиона.
        :param country: Страна, в которой расположен стадион.
        :param city: Город, в котором расположен стадион.
        :param capacity: Вместимость стадиона.
        """
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        """
        Метод для ввода данных о стадионе с клавиатуры.
        """
        self.name = input("Введите название стадиона: ")
        self.opening_date = input("Введите дату открытия: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость стадиона: "))

    def display_data(self):
        """
        Метод для вывода данных о стадионе на экран.
        """
        print(f"Название стадиона: {self.name}")
        print(f"Дата открытия: {self.opening_date}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity} человек")

    def get_name(self):
        """
        Метод для получения названия стадиона.
        """
        return self.name

    def get_opening_date(self):
        """
        Метод для получения даты открытия стадиона.
        """
        return self.opening_date

    def get_country(self):
        """
        Метод для получения страны, в которой расположен стадион.
        """
        return self.country

    def get_city(self):
        """
        Метод для получения города, в котором расположен стадион.
        """
        return self.city

    def get_capacity(self):
        """
        Метод для получения вместимости стадиона.
        """
        return self.capacity


if __name__ == "__main__":
    stadium1 = Stadium()
    stadium1.input_data()

    print("\nИнформация о стадионе:")
    stadium1.display_data()

    # Пример доступа к отдельным полям через методы класса:
    print(f"\nНазвание стадиона: {stadium1.get_name()}")
    print(f"Дата открытия: {stadium1.get_opening_date()}")
    print(f"Страна: {stadium1.get_country()}")
    print(f"Город: {stadium1.get_city()}")
    print(f"Вместимость: {stadium1.get_capacity()} человек")
