# Команды в командной строке или терминале.

# python - вызов интерпретатора python.
# python --version - проверить версию python.
# copyright() - информация об авторских правах.
# licence() - информация о лицензии.
# credits() - информация о благодарностях.
# help() - вызов информации о командах.
# exit() - вход из интерпретатора python.

# Типы данных.

# Строка.
my_str = 'string'
# Целое число.
my_int = 30
# Число с плавающей точкой.
my_float = 12.1
# Логический тип.
my_bool = True
# Список.
my_list = list()
# Словарь.
my_dict = dict()
# Множество.
my_set = set()
# Кортеж.
my_tuple = tuple()
# Диапазон.
my_range = range(100)

# Функция print() в Python, печатает объект, выводит объекты в текстовый поток, отделяя их друг от друга
# ключевым аргументом sep и заканчивая поток аргументом end.
print('print: ', my_str, my_int, my_float, my_bool, my_list, my_dict, my_set, my_tuple, my_range)

# Математические операторы.

x = 10
y = 5
# Сложение.
print('x + y: ', x + y)
# Вычитание.
print('x - y: ', x - y)
# Умножение.
print('x * y: ', x * y)
# Деление.
print('x / y: ', x / y)
# Получение целой части от деления.
print('x // y: ', x // 3)
# Остаток от деления.
print('x % y: ', x % 3)
# Смена знака числа на отрицательный.
print('-x: ', -x)
# Смена знака числа на положительный.
print('+x: ', +x)
# Конвертация булевого значения в целое число.
print('+bool: ', +my_bool)
# Возведение в степень.
print('x ** y: ', x ** y)

# Операторы сравнения.

# Равно.
print('x == y: ', x == y)
# Не равно.
print('x != y: ', x != y)
# Равно.
print('x > y: ', x > y)
# Равно.
print('x < y: ', x < y)

# Логические операторы.

# Оператор НЕ.
print('not y: ', not y)
# Оператор И.
print('x and y: ', x and y)
# Оператор ИЛИ.
print('x or y: ', x or y)
# Оператор проверки совпадения объектов.
print('x is y: ', x is y)
# Оператор отрицания совпадения объектов.
print('x is not y: ', x is not y)
# Оператор проверки нахождения в объекте.
print('x in y: ', x in my_range)
# Оператор отрицания нахождения в объекте.
print('x not in y: ', x not in my_range)

# Преобразование данных.

transform_value = 10
# преобразование целого числа или число с плавающей запятой в строку.
print('str: ', str(transform_value))
# преобразование целого числа или строки в целое число.
print('int: ', int(transform_value))
# преобразование целого числа или строки в число с плавающей запятой.
print('float: ', float(transform_value + 0.1))
# преобразование целого числа в двоичную строку с префиксом 0b.
print('bin: ', bin(transform_value))
# преобразование целого числа в шестнадцатеричную строку с префиксом 0x.
print('hex: ', hex(transform_value))
# преобразование целого числа в восьмеричную строку с префиксом 0o.
print('oct: ', oct(transform_value))
# возвращает логическое значение указанного объекта.
print('bool: ', bool(transform_value))
# возвращает комплексное число с действительной и мнимой частью.
print('complex: ', complex(transform_value))

# Служебные символы.

# Строка в апострофах.
print('string in apostrophes')
# Строка в кавычках.
print("quoted string")
# Строка в многих апострофах если есть апостроф в строке то в кавычках.
print("""It's very big 
string multiline 
block of text""")
# Конкатенация.
print('string one' + ' ' + 'string two')
# \n Перевод строки.
print('line translation: ', 'ab\ncd')
# \ Экранирование.
print('shielding: ', 'ab\\ncd')
# \a Звонок.
print('call: ', 'a\aa')
# \b Забой.
print('slaughter: ', 'ab\ba')
# \f Перевод страницы.
print('page translation: ', 'a\fa')
# \r Возврат каретки.
print('carriage return: ', 'ab\rcd')
# \t Горизонтальная табуляция.
print('horizontal tabulation: ', 'a\ta')
# \v Вертикальная табуляция.
print('vertical tab: ', 'a\va')
# \N{id} Символ Юникода по id.
print('unicode character by id: ', '\N{Degree Sign}')
# \uhhhh 16-ричный символ Юникода.
print('unicode hexadecimal character: ', '\u2030')
# \Uhhhh… 32-ичный символ Юникода.
print('32-character Unicode character: ', '\U00000394')
# \xhh 16-ричное значение символа.
print('hexadecimal character value: ', '\x2A')
# \ooo 8-ричное значение символа.
print('octal value of the character: ', '\275')
# \0 символ Null.
print('null character: ', '\0')

# Методы строк.

str_one = 'my string is very big'
# Переводит первую букву в верхний, а остальные в нижний регистр.
print('capitalize: ', str_one.capitalize())
# Переводит все символы в нижний регистр.
str_two = 'My String is Very big'
print('casefold: ', str_two.casefold())
# Считает количество подстрок str в выбранном промежутке строки.
substring = 'string'
print('count: ', str_one.count(substring))
# # Меняет кодировку строки. По умолчанию возвращает версию строки в кодировке utf-8.
print('encode: ', str_one.encode(encoding='UTF-8', errors='strict'))
# Возвращает True если строка заканчивается на suffix, иначе False.
print('endswith: ', str_one.endswith('string', 3, 9))
# Увеличивает размер символов табуляции до tabsize пробелов.
str_tree = '\tmy\tstr\tis\tvery\tbig'
print('expandtabs: ', str_tree.expandtabs(tabsize=8))
# Возвращает индекс начала первой подстроки str в выбранном промежутке или -1, если она не найдена.
print('find: ', str_one.find('string', 1, 20))
# Возвращает индекс начала последней подстроки str в выбранном промежутке или -1, если она не найдена.
print('rfind: ', str_one.rfind('string', 1, 17))
# Последовательно заменяет {} в строке на свои аргументы. str.format(args, *kwargs)
str_four = 'My {type} is very {value}'
print('format: ', str_four.format(type='string', value='big'))
# Заменяет {<val>} в строке на dict[<val>].
dict_example = {'type': 'string', 'value': 'big'}
print('format_map: ', str_four.format_map(dict_example))
# Возвращает индекс начала первой подстроки str в выбранном промежутке или ValueError, если она не найдена.
print('index: ', str_one.index('string', 1, 20))
# Возвращает индекс начала последней подстроки str в выбранном промежутке или ValueError, если она не найдена.
print('rindex: ', str_one.rindex('string', 1, 20))
# Возвращает True, если строка состоит только из букв и цифр, иначе False.
print('isalnum: ', str_one.isalnum())
# Возвращает True, если строка состоит только из букв, иначе False.
print('isalpha: ', substring.isalpha())
# Возвращает True, если все символы в строке являются десятичными, иначе False.
str_five = '12345'
print('isdecimal: ', str_five.isdecimal())
# Возвращает True, если строка состоит только из цифр, иначе False [1].
print('isdigit: ', str_five.isdigit())
# Возвращает True, если строка является идентификатором (if, class, assert), иначе False.
str_six = 'water'
print('isidentifier water: ', str_six.isidentifier())
# Возвращает True, если вся строка в нижнем регистре, иначе False.
print('islower: ', str_one.islower())
# Возвращает True, если строка состоит только из цифр,
# если в строке есть символы и все они присущи числам (Ⅻ, ⅓, 10), иначе False [1].
print('isnumeric: ', str_five.isnumeric())
# Возвращает True, если все символы строки отображаются, иначе False (например, \n, \t).
print('isprintable: ', str_one.isprintable())
# Возвращает True, если строка состоит из пробелов, иначе False.
print('isspace: ', str_one.isspace())
# Возвращает True, если строка начинается с заглавной буквы, а остальные — строчные, иначе False.
print('istitle: ', str_two.istitle())
# Возвращает True, если строка в верхнем регистре, иначе False.
print('isupper: ', str_two.isupper())
# Склеивает элементы последовательности iter в одну строку с разделителем s.
list_example = ['my', 'string', 'is', 'very', 'big']
print('join method: ', ' '.join(list_example))
# Добавляет в конец строки символ fillchar, пока длина не станет width.
print('ljust: ', str_one.ljust(30, '*'))
# Тоже что и ljust только вправо пока длина не станет width.
print('rjust: ', str_one.rjust(30, '*'))
# Для расширения строки в обоих направлениях как ljust и rjust пока длина не станет width.
print('center: ', str_one.center(30, '*'))
# Переводит символы строки в нижний регистр.
print('lower: ', str_two.lower())
# Возвращает копию строки в верхнем регистре.
print('upper: ', str_one.upper())
# Возвращает строку без пробельных символов или chars в начале и конце.
print('strip: ', str_one.strip('mg'))
# Возвращает строку без пробельных символов или chars в начале.
print('lstrip: ', str_one.lstrip('my'))
# Возвращает строку без пробельных символов или chars в конце.
print('rstrip: ', str_one.rstrip('big'))
# Возвращает таблицу перевода для s.translate. Статический метод str.maketrans создает и возвращает таблицу
# преобразования символов, используемую методом строки str.translate.
# Если существует третий аргумент z, это должна быть строка, символы которой не
# будут отображаться, т.е. будут удаляться.
dict_iterations = {'a': '1', 'm': '2', 'i': '3'}
tbl = str_one.maketrans(dict_iterations)
print('maketrans: ', tbl)
# Заменяет все символы строки согласно таблице перевода.
print('translate: ', str_one.translate(tbl))
# Разделяет строку на три части по первому разделителю sep: [начало, sep, конец].
print('partition: ', str_one.partition('string'))
# Разделяет строку на три части по последнему разделителю sep: [начало, sep, конец].
print('rpartition: ', str_one.rpartition(' '))
# Заменяет все подстроки old на new.
print('replace: ', str_one.replace('string', '123'))
# Возвращает список подстрок, разделенных по sep до maxsplit раз.
print('split full: ', str_one.split())
print('split: ', str_one.split(sep=' ', maxsplit=1))
# Возвращает список подстрок, разделенных по sep до maxsplit раз (с конца).
print('rsplit: ', str_one.rsplit(sep=' ', maxsplit=1))
# Разделяет строку по \n. Не удаляет разделители, если keepends=True.
str_seven = 'my string\nis very big'
print('splitlines: ', str_seven.splitlines(keepends=False))
# возвращает True если строка начинается с prefix, иначе False.
print('startswith: ', str_two.startswith('String', 3, 20))
# Меняет регистр всех символов на противоположный.
print('swapcase: ', str_two.swapcase())
# Возвращает строку, где все слова начинаются с заглавной буквы, а продолжаются строчными.
str_eight = 'MY STRING IS VERY BIG'
print('title: ', str_eight.title())
# Заполняет строку указанным числом нулей в начале.
print('zfill: ', substring.zfill(10))

# Методы списков.

my_list = ['a', 'b', 'c']
print(my_list)
# Удаляет из списка все имеющиеся в нём значения.
my_list.clear()
print('list.clear: ', my_list)
# Добавление множества элементов в список.
my_list.extend(range(10))
print('list.extend: ', my_list)
# Удаление элементов в определенном диапазоне.
del my_list[11:100]
print('del: ', my_list)
# Добавление в список по элементу.
my_list.append(11)
print('list.append: ', my_list)
# Возвращает копию списка. Копия является поверхностной (без рекурсивного копирования элементов).
my_list_two = my_list.copy()
my_list_two.append(12)
print('list.copy: ', my_list, my_list_two)
# Метод count считает количество значений в списке.
counted_el = my_list.count(3)
print('list.count: ', counted_el)
# Метод помогает найти значение индекса элемента в последовательности.
nums = (i for i in range(1, 9))
my_list_two.extend(nums)
index_el = my_list_two.index(3, 12, 19)
print('list.index: ', index_el, ' from ', my_list_two)
# Вставляет указанный элемент перед указанным индексом.
my_list.insert(10, 3)
print('list.insert: ', my_list)
# Возвращает элемент на указанной позиции, удаляя его из списка.
find_el = my_list.pop(10)
print('list.pop: ', find_el)
# Удаляет из списка указанный элемент.
my_list.remove(3)
print('list.remove: ', my_list)
# Перестраивает элементы списка в обратном порядке.
my_list.reverse()
print('list.reverse: ', my_list)
# Сортирует элементы списка на месте.
my_list.append(3)
my_list.sort()
print('list.sort: ', my_list)
# Отсортироват «вручную», так чтобы указанные элементы были в конце.
my_list_two.sort(key=lambda val: val == 7)
print('list.sort to key: ', my_list_two)
# key=None: reverse=False

# Методы словарей.

my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(my_dict)
# Возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default.
print('dict.get: ', my_dict.get(3))
# Создает словарь с ключами из seq и значением value (по умолчанию None).
creating_dict = dict.fromkeys(my_list, 'Value')
print('dict.fromkeys: ', creating_dict)
# Возвращает копию словаря.
my_dict_two = my_dict.copy()
print('dict.copy: ', my_dict_two)
# Очищает словарь.
my_dict_two.clear()
print('dict.clear: ', my_dict_two)
# Возвращает пары (ключ, значение).
print('dict.items: ', my_dict.items())
# Возвращает ключи в словаре.
print('dict.keys: ', my_dict.keys())
# Удаляет ключ, и возвращает значение. Если ключа нет, возвращает default, бросает исключение.
print('dict.pop: ', my_dict.pop(3), my_dict)
# Удаляет и возвращает пару (ключ, значение) с конца словаря. Если словарь пуст, бросает исключение.
print('dict.popitem: ', my_dict.popitem(), my_dict)
# Возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default.
# setdefault() устанавливает отсутствующие ключи в словаре.
# get() предоставляет только значение по умолчанию, но не изменяет словарь.
print('dict.setdefault: ', my_dict.setdefault(1))
# Обновляет словарь, добавляя пары (ключ, значение). Существующие ключи перезаписываются. Возвращает None.
my_dict_tree = {1: 'Tom', 2: 'Carl', 3: 'James'}
print('dict.update: ', my_dict.update(my_dict_tree), my_dict)
# Возвращает значения в словаре.
print('dict.values: ', my_dict.values())

# Методы множеств.

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
my_set_two = {10, 20, 30, 40, 50, 60, 70, 80, 90}
print(my_set, my_set_two)
# Истина, если set и other не имеют общих элементов.
returned_isjoint = my_set.isdisjoint(my_set_two)
print('set.isdisjoint: ', returned_isjoint)
# Все элементы set принадлежат other, все элементы other принадлежат set.
compared_sets = my_set == my_set_two
print('compared sets: ', compared_sets)
# Или set <= other - все элементы set принадлежат other.
less_or_equal = my_set.issubset(my_set_two)
print('less or equal: ', less_or_equal)
# Или set >= other - аналогично.
greater_or_equal = my_set.issuperset(my_set_two)
print('greater or equal: ', greater_or_equal)
# Или set | other | объединение нескольких множеств.
my_set = my_set.union(my_set_two)
print('set.union: ', my_set)
# Или set & other & пересечение.
my_set_tree = {10, 20, 30, 100, 200}
intersected_el = my_set.intersection(my_set_tree)
print('set.intersection: ', intersected_el)
# Или set - other множество из всех элементов set, не принадлежащие ни одному из other.
differenced_sets = my_set.difference(my_set_tree)
print('set.difference: ', differenced_sets)
# Или set ^ other множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
symmetric_differenced_sets = my_set.symmetric_difference(my_set_tree)
print('set.symmetric_difference: ', symmetric_differenced_sets)
# Копия множества.
my_set_four = my_set.copy()
print('set.copy: ', my_set_four)
# Операции изменяющие множество:
# Или set |= other | объединение.
my_set_tree.update(my_set_four)
print('set.update: ', my_set_tree)
# Или set &= other & ... - пересечение.
my_set_five = {100, 200, 300, 400, 500}
my_set_five.intersection_update(my_set_tree)
print('set.intersection_update: ', my_set_five)
# Или set -= other | вычитание.
my_set_tree.difference_update(my_set_five)
print('set.difference_update: ', my_set_tree)
# Или set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
my_set_five.symmetric_difference_update(my_set_tree)
print('set.symmetric_difference_update: ', my_set_five)
# Добавляет элемент в множество.
my_set_five.add(1000)
print('set.add: ', my_set_five)
# Удаляет элемент из множества. KeyError, если такого элемента не существует.
my_set_five.remove(1000)
print('set.remove: ', my_set_five)
# Удаляет элемент, если он находится в множестве.
my_set_five.discard(200)
print('set.discard: ', my_set_five)
# Удаляет первый элемент из множества.
# Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
my_set_five.pop()
print('set.pop: ', my_set_five)
# Очистка множества.
my_set_five.clear()
print('set.clear: ', my_set_five)
# Класс frozenset преобразует строку или любую последовательность(итерацию) в неизменяемое множество.
# Отличие set от frozenset в том, что set - изменяемый тип данных, а frozenset - нет.
my_set_five = frozenset('abcdefgh')
print('frozenset: ', my_set_five)

# Методы кортежей.

# Все операции над списками, не изменяющие список.
# Сложение, умножение на число, методы index() и count() и др. Можно менять элементы местами.
my_tuple = tuple('hello, world!')
my_tuple_two = ('hello', 'world')
print(my_tuple, my_tuple_two, type(my_tuple), type(my_tuple_two))


# Обработка ошибок.
# Генерация ошибки с помощью raise.
def check_nums(a, b):
    if b == 0:
        raise TypeError('Second argument can not be zero')
    return a / b


# Выполнение блока кода.
try:
    check_nums(10, 0)
# Этот код выполняется в случаеш ошибок TypeError в блоке try.
# Присвоит ошибку как значение в переменную при помощи as.
# TypeError указывается для ошибок связанные с типами данных.
# Exception указывается если неизвестна ошибка или же (не рекомендуется) ничего не прописывается.
except ZeroDivisionError as error_text_one:
    print('Trying 10 / 0')
    # Вывести в терминал текстовое описание ошибки.
    print('error: ', error_text_one)
# В случае применения raise сработает этот блок кода.
except TypeError as error_text_two:
    print('error: ', error_text_two)
# В блоке else код выполниться если ошибок нет.
else:
    print('Code without errors.')
# Этот блок кода выполниться в любом случае после блока try.
finally:
    print('Code is continue')
