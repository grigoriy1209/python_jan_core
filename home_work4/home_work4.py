# 1) Є ось такий файл email.txt ваша задача записати в новий файл тільки email'ли з доменом gmail.com
# (Хеш то що з ліва записувати не потрібно))
try:
    with open('email.txt', 'r') as file, open('gmail.txt', 'w') as outfile:
        for line in file:

            parts = line.strip().split()
            if len(parts) > 1:
                email = parts[1]

                if email.lower().endswith('@gmail.com'):
                    print(email, file=outfile)
except Exception as e:
    print(e)

# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
#  - всі покупки зберігаємо в файлі
# з функціоналу:
# * вивід всіх покупок
# * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

import json
from typing import TypedDict, List

Shopping_Cart = TypedDict('Shopping_Cart', {'id': int, 'title': str, 'price': int})


class Notebook:
    def __init__(self):
        self.__filename = input('enter filename: ')
        self.__notes_data: List[Shopping_Cart] = []
        self.__read_notes()

    def __read_notes(self):
        try:
            with open(self.__filename, 'r') as f:
                self.__notes_data =  json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

    def __save_notes(self):
        try:
            with open(self.__filename, 'w') as f:
                json.dump(self.__notes_data, f)
        except Exception as err:
            print(err)

    def __display_all(self):
        if not self.__notes_data:
            print('There are no shopping carts')
            return
        for shopping_cart in self.__notes_data:
            print(f'id:{shopping_cart["id"]}, prise:{shopping_cart["price"]}, title:{shopping_cart["title"]}')

    def __show_all(self):
        for item in self.__notes_data:
            print(item)

    def __add_note(self):
        try:
            cart_id = int(input('enter cart id: '))
            title = input('Enter title: ')
            price = int(input('Enter price: '))
            new_note = Shopping_Cart(title=title, price=price, id=cart_id)
            self.__notes_data.append(new_note)
            self.__save_notes()
            print('Added new shopping cart')
        except KeyboardInterrupt:
            print('User cancelled.')

    def search_note(self):
        search_results = input('Enter search term: ')
        for item in self.__notes_data:
            for value in item.values():
                if search_results == str(value):
                    print(item)

    def __delete_note_by_id(self):
        self.__show_all()
        try:
            pk = int(input('Enter id: '))
            index = next((index for index, v in enumerate(self.__notes_data) if v['id'] == pk), None)
            if index is None:
                print('No  id found.')
                return
            del self.__notes_data[index]
            self.__save_notes()
        except ValueError:
            print('Invalid id.')

    def menu(self):
        while True:
            print('\nMenu:')
            print('1. get all cart')
            print('2. add cart')
            print('3. search cart')
            print('4. delete cart')
            print('5. display all cart')
            print('6. Exit')

            choice = input('Enter your choice: ')

            match choice:
                case '1':
                    self.__read_notes()
                case '2':
                    self.__add_note()
                case '3':
                    self.search_note()
                case '4':
                    self.__delete_note_by_id()
                case '5':
                    self.__display_all()
                case '6':
                    break


notebook = Notebook()
notebook.menu()