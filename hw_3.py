from typing import Self
from abc import abstractmethod, ABC


# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
# + сумма площин двох екземплярів класу
# - різниця площин двох екземплярів класу
# == площин на рівність
# ! = площин на не рівність
# >, < меньше більше
# при виклику метода len() підраховувати сумму сторін


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, other: Self):
        return self.area + other.area

    def __sub__(self, other: Self):
        return self.area - other.area

    def __eq__(self, other: Self):
        return self.area == other.area

    def __ne__(self, other: Self):
        return self.area != other.area

    def __gt__(self, other: Self):
        return self.area > other.area

    def __lt__(self, other: Self):
        return self.area < other.area

    def __len__(self, other: Self):
        return (self.x + other.y) * 2


# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту сaму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __counter = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__counter += 1

    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def get_counter(cls):
        cls.__counter += 1
        print(cls.__counter)


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_list_cinderella(self, cinderellas: list[Cinderella]) -> None:
        for cinderella in cinderellas:
            if cinderella.foot_size == self.shoe_size:
                print(cinderella)
                return


cinderellas_arr: list[Cinderella] = [
    Cinderella(name="Valia", age=20, foot_size=38),
    Cinderella(name="Camila", age=40, foot_size=39),
    Cinderella(name="Vanila", age=50, foot_size=45),
    Cinderella(name="Paulina", age=60, foot_size=47),
]
prince = Prince("Petro", 20, 39)
prince.find_list_cinderella(cinderellas_arr)
print(Cinderella.get_counter())


# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book
# або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
#  - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу


class Printable(ABC):

    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'Book: {self.name}')


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'Magazine: {self.name}')


class Main:
    __printtable_list: list[Printable] = []

    @classmethod
    def add(cls, value):
        if isinstance(value, Printable):
            cls.__printtable_list.append(value)

    @classmethod
    def show_all_magazines(cls):
        for magazine in cls.__printtable_list:
            if isinstance(magazine, Magazine):
                magazine.print()

    @classmethod
    def show_all_books(cls):
        for book in cls.__printtable_list:
            if isinstance(book, Book):
                book.print()


# Приклад:
#
Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))
Main.add(Book('Book2'))
Main.add(Book('Book2'))


print('-' * 40)
Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()

