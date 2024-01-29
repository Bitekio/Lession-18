"""
Hw4
"""


class MainClass:
    """class main"""
    def __init__(self, text):
        self.text_field = text

    def set_text_field(self, new_text=""):
        """
        Метод для присваивания значения текстовому полю.

        :param new_text: Новое значение для текстового поля.
        """
        self.text_field = new_text

    def get_text_field(self):
        """
        Метод для получения значения текстового поля.

        :return: Текущее значение текстового поля.
        """
        return self.text_field


class ChildClass(MainClass):
    def __init__(self, text, number):
        """
        Конструктор класса-потомка.

        :param text: Текстовый аргумент для главного класса.
        :param number: Числовой аргумент для класса-потомка.
        """
        super().__init__(text)
        self.number_field = number

    def set_number_field(self, new_number):
        """
        Метод для присваивания значения числовому полю.

        :param new_number: Новое значение для числового поля.
        """
        self.number_field = new_number

    def get_number_field(self):
        """
        Метод для получения значения числового поля.

        :return: Текущее значение числового поля.
        """
        return self.number_field


if __name__ == "__main__":
    main_obj = MainClass("Hello")
    print("Текстовое поле главного класса:", main_obj.get_text_field())

    main_obj.set_text_field("New Text")
    print("Обновленное текстовое поле главного класса:", main_obj.get_text_field())

    child_obj = ChildClass("Child Text", 42)
    print("\nТекстовое поле класса-потомка:", child_obj.get_text_field())
    print("Числовое поле класса-потомка:", child_obj.get_number_field())

    child_obj.set_text_field("Updated Child Text")
    child_obj.set_number_field(99)

    print("\nОбновленное текстовое поле класса-потомка:", child_obj.get_text_field())
    print("Обновленное числовое поле класса-потомка:", child_obj.get_number_field())
