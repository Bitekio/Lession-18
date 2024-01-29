"""
hw1
"""


class Car:
    """class car"""
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        """
        Инициализация объекта класса Car.

        :param model: Название модели автомобиля.
        :param year: Год выпуска автомобиля.
        :param manufacturer: Производитель автомобиля.
        :param engine_volume: Объем двигателя автомобиля в литрах.
        :param color: Цвет автомобиля.
        :param price: Цена автомобиля в рублях.
        """
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        """
        Метод для ввода данных об автомобиле с клавиатуры.
        """
        self.model = input("Введите модель автомобиля: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_volume = float(input("Введите объем двигателя: "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def display_data(self):
        """
        Метод для вывода данных об автомобиле на экран.
        """
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_volume} л")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price} руб.")

    def get_model(self):
        """
        Метод для получения названия модели автомобиля.
        """
        return self.model

    def get_year(self):
        """
        Метод для получения года выпуска автомобиля.
        """
        return self.year

    def get_manufacturer(self):
        """
        Метод для получения производителя автомобиля.
        """
        return self.manufacturer

    def get_engine_volume(self):
        """
        Метод для получения объема двигателя автомобиля.
        """
        return self.engine_volume

    def get_color(self):
        """
        Метод для получения цвета автомобиля.
        """
        return self.color

    def get_price(self):
        """
        Метод для получения цены автомобиля.
        """
        return self.price


if __name__ == "__main__":
    car1 = Car()
    car1.input_data()

    print("\nИнформация о машине:")
    car1.display_data()

    print(f"\nМодель автомобиля: {car1.get_model()}")
    print(f"Год выпуска: {car1.get_year()}")
    print(f"Производитель: {car1.get_manufacturer()}")
    print(f"Объем двигателя: {car1.get_engine_volume()} л")
    print(f"Цвет машины: {car1.get_color()}")
    print(f"Цена: {car1.get_price()} руб.")
