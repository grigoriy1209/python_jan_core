# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання

from typing import Callable


def notebook() -> tuple[Callable[[str], None],                           #типізація для add_todo
                        Callable[[], list[str]],                            #типізація для get_all
                        Callable[[str], None]]:                              #типізація для delete
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    def delete_todo(todo: str) -> None:
        nonlocal todo_list
        if todo in todo_list:
            todo_list.remove(todo)

    return add_todo, get_all, delete_todo


add_todos, get_alls, delete = notebook()

add_todos('start')
add_todos('end')
delete('start')
print(get_alls())

# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

# Приклад:

# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій