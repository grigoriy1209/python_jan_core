# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 ffhgfhgfh343565dfdg544'
print(','.join(ch for ch in st if ch.isdigit()))

#################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# введена строка
# 23, 544, 34              #вивело в консолі
st = 'as 23 fdfdg544 34'
print(', '.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))
#################################################################################

# list comprehension
#
# 1)є строка:
greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
print([ch.upper() for ch in greeting])
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
res = [i ** 2 for i in range(50) if i % 2]
print(res)


# function
#
# - створити функцію яка виводить ліст

def print_list(lst):
    for i in lst:
        print(i)


list1 = [1, 2, 3, 4, 5]
print_list(list1)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def num_max(a, b, c):
    max_num = max(a, b, c)
    print(f" max number:{max_num}")
    return max_num


result = num_max(23, 45, 20)
print(result)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def n_num(*args):
    max_num = max(args)
    min_num = min(args)
    print(f" max number- {max_num}")
    return min_num


result1 = n_num(1, 2, 3, 47)
print(result1)


# - створити функцію яка повертає найбільше число з ліста
def max_num_list(num):
    max_num = max(num)
    return max_num


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 4459, 10]
result2 = max_num_list(numbers)
print(f" max number=={result2}")


# - створити функцію яка повертає найменьше число з ліста
def min_num_list(num):
    min_num = min(num)
    return min_num


numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 4459, 10]
result3 = min_num_list(numbers1)
print(f" min number=={result3}")


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_num_list(num):
    num_sum = sum(num)
    return num_sum


result4 = sum_num_list(numbers1)
print(f" sum number=={result4}")


#  - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def avg_num_list(num):
    avg_num = sum(num)
    avg_num = avg_num / len(num)
    return avg_num


result5 = avg_num_list(numbers1)
print(f" avg number=={result5}")

################################################################################################
# 1)Дан list:
list_arr = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


# # - знайти мін число
def min_num_list():
    min_num = min(list_arr)
    print(f" min num{min_num}")


# # - видалити усі дублікати
def dublicate_list():
    print(set(list_arr))


# - замінити кожне 4-те значення на 'X'
def update_list():
    print(['X' if not (i + 1) % 4 else item for i, item in enumerate(list_arr)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('  *' * n)
        else:
            print(' *' + '    ' * (n - 2) + ' * ')


# 3) вывести табличку множення за допомогою цикла while
def table_multiplication():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            print(f'{i * j:4}', end="")
            j += 1
        print()
        i += 1


# 4) переробити це завдання під меню
while True:
    print('1:знайти мін число')
    print('2:видалити усі дублікати')
    print('3:замінити кожне 4-те значення на X')
    print('4: вивести квадрат ')
    print('5:вывести табличку множення')
    print('6:the end')

    choice = input('зробіть ваш вибір: ')
    if choice == '1':
        min_num_list()
    elif choice == '2':
        dublicate_list()
    elif choice == '3':
        update_list()
    elif choice == '4':
        square(7)
    elif choice == '5':
        table_multiplication()
    elif choice == '6':
        break
