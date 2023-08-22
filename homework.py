from datetime import time


def test_dark_theme_by_time():
    """
    Проверка: правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=14)
    # Переключение на темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    if time(hour=6) < current_time < time(hour=22):
        is_dark_theme = False

    else:
        is_dark_theme = True

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Проверка: правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    is_dark_theme = None
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # Темная тема переключена пользователем
    if dark_theme_enabled_by_user:
        is_dark_theme = True
    # Темная тема не переключена пользователем
    elif not dark_theme_enabled_by_user:
        is_dark_theme = False
    # Пользователь не сделал выбор
    elif dark_theme_enabled_by_user is None:
        if  current_time < time(hour=6) or current_time >= time(hour=22):
            is_dark_theme = True
        else:
            is_dark_theme = False

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Проверка: Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # Найти пользователя с именем Olga
    for user in users:
       if users["name"] == 'Olga':
           suitable_users = user

    assert suitable_users == {"name": "Olga", "age": 45}

    # Найти всех пользователей младше 20 лет
    suitable_users = []
    for user in users:
       if users["age"] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]

# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"
def read_function(func, *args):
    name = func.__name__.replace("_", " ").title()
    arg = ', '.join(args)
    result = f'{name} [{arg}]'
    print
    return result

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def open_browser(browser_name):
    actual_result = read_function(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"

def go_to_companyname_homepage(page_url):
    actual_result = read_function(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = read_function(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
