int_value = 30
str_value = 'string'
list_value = []
dict_value = dict()
set_value = set()
range_value = range(100)

# Создание цикла for.
for i in range_value:
    list_value.append(i)

print('for cycle: ', list_value)

# Создание цикла while.
while len(set_value) == 0:
    for i in list_value:
        set_value.add(i)

print('while cycle: ', set_value)


# Создание функции. *args: Позиционные аргументы. **kwargs : Именованные аргументы.
def my_func(massive, number):
    # Обьявление глобальной переменной.
    global range_value
    # Создание цикла while.
    while len(massive) == 0:
        # Создание цикла for.
        for i in range_value:
            # Создание условия.
            if number == 30:
                massive = ['a', 'b', 'c']
            elif number != 30:
                return None
            else:
                return None
    # Функция возвращает переменную.
    return massive


# Условие одной строкой.
condition_run = 5 + 10 if 10 < 20 else 5 - 2
print('if else in one string: ', condition_run)

# Цикл for одной строкой.
cycle_values = (i for i in range(20))
cycle_list = list(cycle_values)
print('cycle in one string: ', cycle_list)

# Вызов функции.
value_in_func = my_func(list_value, int_value)
print('function: ', value_in_func)

# Лямбда функция.
example_value = 20
lambda_function = lambda lambda_value_one, lambda_value_two: lambda_value_one * lambda_value_two
print('lambda function: ', lambda_function(20, 5))


# Замыкание на лямбда функции.
# Явное указание типа аргумента в скобках.
def greeting(greet: str):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting('Good norning')
print('lambda closure: ', morning_greeting('Thomas'))


# Функция возвращающая генератор.
# Генераторы также относятся к итерируемым объектам, однако данные из них можно считать только один раз.
# Генераторы не хранят значения в памяти, а создают их на лету.
# Генератор вычисляя каждый последующий элемент, «забывает» о предыдущем.
def create_generator(massive):
    list_generator = massive
    for i in list_generator:
        yield i * 2


my_list_tree = []
my_list_tree.extend(create_generator(value_in_func))
print('yield: ', my_list_tree)

# Базовые методы и функции Python.

# Определение типа данных. Класс type с тремя аргументами вернет объект нового типа.
print('type: ', type(int_value), type(str_value), type(list_value), type(dict_value), type(range_value))
# Функция len() в Python, количество элементов объекта, возвращает длину (количество элементов) в объекте.
# Аргумент может быть последовательностью или коллекцией.
print('len: ', len(str_value), len(list_value), len(dict_value), len(set_value), len(range_value))
# Функция next() в Python, следующий элемент итератора, возвращает следующий элемент
# итератора, вызвав его метод __next__().
mygenerator = create_generator(value_in_func)
print('next: ', next(mygenerator), next(mygenerator), next(mygenerator))
# Функция iter создает итератор из последовательности.
# object - последовательность или итератор.
# sentinel - значение с которым будет вызываться каждый элемент из object если это вызываемые объекты.
iterible_value = iter(list_value)
print('iter: ', next(iterible_value), next(iterible_value), next(iterible_value))
# Функция abs() в Python, абсолютное значение числа, преобразует целое число или число с плавающей запятой
# в его абсолютное значение.
print('abs: ', abs(int_value))
# Функция all() в Python, все элементы True, возвращает значение True , если все элементы в итераторе истинны,
# в противном случае она возвращает значение False
list_value.append(False)
print('all: ', list_value, all(list_value))
# Функция any() в Python, хотя бы один элемент True, возвращает True, если какой - либо (любой) элемент
# в итерируемом объекте True, в противном случае any() возвращает значение False.
list_value.append(True)
print('any: ', list_value, any(list_value))
# Функция ascii() в Python, преобразует строку в ASCII, возвращает строку, содержащую печатаемое
# представление объекта(читаемую версию) с экранированными не-ASCII символами.
line = 'My name is Антон'
print('ascii: ', ascii(line))
# Класс bytes() в Python, преобразует в строку байтов, возвращает байтовый объект bytes, который является
# неизменяемой последовательностью целых чисел в диапазоне от 0 <= х <256.
prime_numbers = [50, 100, 76, 72, 41]
print('bytes: ', bytes(prime_numbers))
# Класс bytearray() в Python, преобразует в массив байтов, возвращает массив байтов bytearray,
# который является изменяемой последовательностью целых чисел в диапазоне от 0 <= х <256.
print('bytearray: ', bytearray([2, 3, 5, 7]))
# Функция callable() в Python, проверяет можно ли вызвать объект, возвращает True,
# если указанный объект вызываемый, в противном случае она возвращает значение False.
print('callable: ', callable(str_value))
# Функция chr() в Python, число в символ Юникода, вернет строку, представляющую символ,
# соответствующий переданному в качестве аргумента целому числу из таблицы символов Unicode.
# Допустимый диапазон аргументов - от 0 до 1114111
print('chr: ', chr(100))
# Функция eval() в Python, выполняет строку-выражение с кодом, выполняет строку-выражение,
# переданную ей в качестве обязательного аргумента и возвращает результат выполнения этой строки.
eval_value = 'print("eval: 5 + 10 =", (5+10))'
eval(eval_value)
# Функция exec() в Python, выполняет блок кода, поддерживает динамическое выполнение кода Python.
# Передаваемый в качестве аргумента объект должен быть либо строкой, либо объектом кода.
globals_dict = {'x': 5}
locals_dict = {}
code = "y = x ** 2"
exec(code, globals_dict, locals_dict)
print('exec: ', locals_dict['y'])
# Функция compile() компилирует блок кода Python, возвращает переданный, в качестве аргумента источник,
# в виде объекта кода, готового к выполнению.
# Параметры: compile(source, filename, mode, flag, dont_inherit, optimize)
# source - обязательный параметр. Может быть обычной строкой, байтовой строкой,
# либо объектом абстрактного синтаксического дерева.
# filename - обязательный параметр. Имя файла, из которого будет читается код.
# Если код не будет считан из файла, вы можете написать в качестве параметра любую строку <string>.
# mode - обязательный параметр. Может принимать 3 значения:
# eval, если источником является одно выражение;
# exec,если источником является блок операторов;
# single, если код состоит из одного оператора;
# flag - необязательный параметр. По умолчанию flags=0 и определяет, будет ли скомпилированный код
# содержать асинхронные операции или какие инструкции из __future__ следует использовать.
# Указывается битами. Если нужно задать несколько инструкций, то их можно указывать через or;
# dont_inherit - необязательный параметр. По умолчанию dont_inherit=False. Указывает, следует ли
# использовать future определенные в коде, в дополнение в тем, что указаны во flags;
# optimize - необязательный параметр. По умолчанию optimize=-1.
# Задаёт уровень оптимизации компилятора:
# -1 — использовать настройки интерпретатора (регулируются опцией -O);
# 0 — не оптимизировать, включить debug;
# 1 — убрать инструкции asserts, выключить debug;
# 2 — то, что делает 1 + убрать строки документации.
eval(compile("print('compile: 4 + 5 =', 4+5)", 'test', 'eval'))
# Функция dir() в Python, все атрибуты объекта, вызванная без аргумента, возвращает список имен в
# текущей локальной области, а вызванная с аргументом попытается вернуть список
# допустимых атрибутов для указанного объекта.
print('dir: ', dir(list))
# Функция divmod() в Python, делит числа с остатком, возвращает кортеж, содержащий частное и остаток.
# Не поддерживает комплексные числа. Со смешанными типами операндов применяются правила для
# двоичных арифметических операторов.
print('divmod: ', divmod(19, 5))
# Функция enumerate() в Python, счетчик элементов последовательности, возвращает кортеж, содержащий
# пары ('счётчик', 'элемент') для элементов указанного объекта.
enum_value = enumerate(prime_numbers)
print('enumerate: ', list(enum_value))
# Функция filter() в Python, фильтрует список по условию, фильтрует элементы переданного объекта при помощи
# пользовательской функции. Принимает в качестве аргументов пользовательскую фильтрующую
# функцию и объект, элементы которого следует отфильтровать.
numbers = [1, 2, 4, 5, 7, 8, 10, 11]


# функция, которая проверяет четные или нечетные числа.
def filter_odd_num(in_num):
    if (in_num % 2) == 0:
        return True
    else:
        return False


# Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)
print('filter: ', list(out_filter))
# Функция format() в Python, форматирует значение переменной, преобразует переданное значение в
# отформатированную строку, в соответствии с спецификацией формата Mini-Language
print('format: ')
# Функция hash() в Python, хэш-значение объекта, возвращает хэш-значение объекта, если оно есть.
print('hash: ')
# Функция id() в Python, идентификатор объекта, возвращает уникальный идентификатор для указанного объекта.
print('id: ', id(int_value))
# Функция globals() в Python, переменные глобальной области, возвращает словарь со значениями переменных,
# представляющий текущую глобальную область видимости модуля.
print('globals: ')
# Функция locals() в Python, переменные локальной области, обновляет и возвращает словарь с
# переменными и их значениями из текущей локальной области видимости.
print('locals: ')
# Функция map() в Python, обработка последовательности без цикла, выполняет пользовательскую функцию
# для каждого элемента последовательности, коллекции или итератора.
print('map: ')
# Функция min() в Python, минимальное значение элемента, наименьшее число из итерируемого объекта
# или самое маленькое из двух или более переданных позиционных аргументов.
print('min: ', min(prime_numbers))
# Функция max() в Python, максимальное значение элемента, вернет наибольшее число из итерируемого объекта
# или самое большое из двух или более переданных позиционных аргументов.
print('max: ', max(prime_numbers))
# Класс memoryview() в Python, ссылка на буфер обмена, возвращает ссылку на буфер обмена памяти,
# в которой находится переданный в качестве аргумента объект.
# Объект obj должен поддерживать протокол буфера обмена.
data = b"world"
buffer_view = memoryview(data)
print('memoryview: ', list(buffer_view))
# Функция open() в Python, открывает файл на чтение/запись, открывает файл для чтения или записи при помощи
# файлового потока. Если файл не может быть открыт, бросается исключение OSError.
# file – путь к файлу (вместе с его именем); "C:/Python/data.txt" или data.txt.
# mode – режим доступа к файлу (чтение/запись);
# encoding – кодировка файла.
# newline - как работает режим новой строки (доступные значения: None, ' ', '\n', 'r' и '\r\n')
# errors - строка, указывающая, как обрабатывать ошибки кодирования/декодирования.
# buffering - используется для настройки политики буферизации.
# opener (опционально) - настраиваемый открывалка; должен вернуть дескриптор открытого файла.
# r - открытие файла на чтение. (дефолт)
# w - открытие файла на запись, содержимое файла удаляется, если файла не существует, создается новый.
# x - открытие файла на запись, если файла не существует. Если файл существует, возникает исключение.
# b - открытие файла в двоичном режиме.
# t - открытие файла в текстовом режиме. (дефолт)
# + - открытие файла на чтение и запись.
# Создаем файл и записываем в него текст.
file_one = open('data.txt', mode='w', encoding="utf-8")
# write(content) - Записывает информацию в файл.
text_to_write = """На этом занятии мы с вами научимся читать данные из файлов.
Начнем со знакомства с функцией.
Например, вот такая запись."""
file_one.write(text_to_write)
file_one.close()
# open() - открывает файл для чтения.
file_one = open('data.txt', encoding="utf-8")
# Чтение файла полностью. В скобках можно указать первые символы.
print('open: ', file_one.read())
# tell() - Возвращает текущий указатель внутри файла.
print('tell:', file_one.tell())
# seek(position, from_what=0) - Перемещает указатель в заданную позицию.
file_one.seek(0)
print('seek:', file_one.seek(0))
# readline() - считывает одну строку из файла.
first_line = file_one.readline()
print('readline:', first_line.rstrip('\n'))
# readlines() - считывает все строки файла в список.
all_lines = file_one.readlines()
print('readlines:')
for line in all_lines:
    print(line.strip())
# Закрытие файла close(). Обязательно вызывать этот метод после окончания работы с файлом.
file_one.close()
# Функция ord() в Python, число символа Unicode, для символа x вернет число, из таблицы символов Unicode
# представляющее его позицию. Функция ord() обратная chr().
print('ord: ', ord('h'))
# Функция reversed() в Python, разворачивает последовательность, возвращает обратный итератор, то есть
# возвращает итератор, который перебирает элементы оригинала в обратном порядке, reversed не создает
# копию и не изменяет оригинал последовательности.
reversedity = ''.join(reversed(str_value))
print('reversed: ', reversedity)
# Функция round() в Python, округляет число, вернет число, округленное до точности ndigits после
# десятичной точки. Если аргумент ndigits опущен или None, то вернет ближайшее целое число.
float_num = 1.7
print('round: ', round(float_num))
# Класс slice() в Python, шаблон среза, вернет срез/часть итерируемого объекта,
# которая будет следовать шаблону, указанному в аргументах.
# start - тип int, начальный индекс среза;
# stop - тип int, конечный индекс среза (не будет входить в конечный результат);
# step - тип int, шаг, с которым нужно выбирать элементы.
# slice(start, stop, step)
sliced = slice(1, 5)
print('slice: ', str_value[sliced])
# Функция sorted() в Python, выполняет сортировку, вернет новый отсортированный список из
# итерируемых элементов. Функция имеет два необязательных аргумента, которые
# должны быть указаны в качестве аргументов ключевых слов.
print('sorted: ', sorted(prime_numbers))
# Функция sum() в Python, сумма последовательности, начинает суммирование элементов последовательности с
# начального значения start, сложение происходит лева на право и в результате возвращает их сумму.
numbers = [1, 2, 3, 4, 5]
print('sum: ', sum(numbers))
# Функция divmod() возвращает кортеж, содержащий частное и остаток. Не поддерживает комплексные числа.
# Со смешанными типами операндов применяются правила для двоичных арифметических операторов.
# Пара (x // y, x % y).
number_one = 2
number_two = 3
print('divmod: ', divmod(number_one, number_two))
# Функция pow() в Python, возводит число в степень, возвращает результат возведения числа base в
# степень exp, с опциональным делением по модулю mod. Когда параметр z указан, функция pow(x, y, z) вернет
# остаток от деления результата возведения x в степень y на z.
print('pow(2, 3): ', pow(2, 3))
print('pow(2, 3, 5): ', pow(2, 3, 5))
# Функция zip() в Python, объединить элементы в список кортежей, создает итератор кортежей, который
# объединяет элементы из каждой из переданных последовательностей.
zip_value = zip(value_in_func, prime_numbers)
print('zip: ', dict(zip_value))
# Функция input() в Python, ввод данных с клавиатуры, позволяет обеспечить ввод пользовательских
# данных с консоли. Считывает строку данных, полученную с устройства ввода.
input_value = input('Enter any: ')
print('input: ', input_value)
# Функция help() в Python, справка по любому объекту, вызывает встроенную справочную систему.
# Эта функция предназначена для интерактивного использования.
print('help: ', help(id))
# Функция breakpoint() в Python, отладчик кода, обеспечивает удобство использования отладчика, поскольку нам
# не нужно явно импортировать pdb модуль, а так же писать дополнительный код, чтобы войти в отладчик.
breakpoint()
print('breakpoint: ', str_value)
