# Реализованные некоторые функции из книги "Python. Книга рецептов" Дэвида Бизли и Брайана К. Джонса.

import heapq
from collections import defaultdict, OrderedDict, Counter

# Распаковка последовательности в отдельные переменные.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a, b, c, d, e, f, g, _, _, _ = my_list
print('unpacked list: ', a, b, c, d, e, f, g, ' from ', my_list)

# Распаковка элементов из последовательностей произвольной длины.
a, b, c, d, e, f, g, *another_values = my_list
print('unpacked list with arbitrary length: ', a, b, c, d, e, f, g, another_values, ' from ', my_list)

# Распаковка элементов с последним значением.
*trailing, current = my_list
print('unpacked list with last value: ', trailing, current, ' from ', my_list)

# Расширенная распаковка подходит для распаковки итерируемых объектов неизвестной или произвольной длины.
record_one = [('foo', 1, 2), ('bar', 'hello', 10, 4), ('cat', 5, 2, 30, 700)]
tags_tuple = dict((tag, [*args]) for tag, *args in record_one)
print('unpacked massive tuples: ', record_one, ' to ', tags_tuple)

# Распаковка со звездочкой может быть полезна в комбинации с операциями обработки строк, например разрезание.
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedirectory, sh = line.split(':')
print('unpacked slides strings: ', uname, 'and', *fields, ' and ', homedirectory, ' and ', sh)

# Распаковка где можно использовать обычное для отбрасывания имя переменной, такое как _ или ign.
record_two = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record_two
print(name, year)

# Поиск N максимальных и минимальных элементов.
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# Эти же функции параметром key, для работы с более сложными структурами данных.
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]
print(heapq.nsmallest(3, portfolio, key=lambda s: s['price']))
print(heapq.nlargest(3, portfolio, key=lambda s: s['price']))


# Реализация очереди с приоритетом.
def priority_queue():
    elements = []

    def add_task(task, priority):
        heapq.heappush(elements, (priority, task))

    def pop_task():
        return heapq.heappop(elements)[1]

    task_value = add_task
    pop_value = pop_task
    return task_value, pop_value


task_func, pop_func = priority_queue()
task_func('task1', 2)
task_func('task2', 1)
task_func('task3', 3)
print(pop_func(), pop_func(), pop_func())

# Отображение ключей на несколько значений в словаре и добавление новых значений.
d_dict = defaultdict(list, {'a': [1, 2, 3], 'b': [4, 5]})
e_dict = defaultdict(set, {'a': {1, 2, 3}, 'b': {4, 5}})
d_dict['a'].append(6)
e_dict['a'].add(9)
print(d_dict, e_dict)

# Поддержание порядка в словарях, где контролировать порядок элементов при итерировании или сериализации.
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)

# Перемещение элемента в конец.
ordered_dict.move_to_end('a')
print(ordered_dict)

# Извлечение последнего элемента
last_item = ordered_dict.popitem()
print(last_item, ordered_dict)

# Вычисления со словарями. Поиск минимального и максимального значений.
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(max_price, min_price)

# Поиск общих элементов в двух словарях.
f_dict = {'x': 1, 'y': 2, 'z': 3}
g_dict = {'w': 10, 'x': 11, 'y': 2}
# Найти общие ключи.
print(f_dict.keys() & g_dict.keys())
# Найти ключи, которые есть в f_dict, но которых нет в g_dict.
print(f_dict.keys() - g_dict.keys())
# Найти общие пары key, value.
print(f_dict.items() & g_dict.items())


# Удаление дубликатов из последовательности с сохранением порядка элементов.
def dedupe_two(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


dedupe_list = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe_two(dedupe_list)))

# Присваивание имен срезам.
record = '....................100 .......513.25 ..........'
slice_one = slice(20, 28)
slice_two = slice(29, 40)
cost_str = record[slice_one].strip('. ').strip()
price_str = record[slice_two].strip('. ').strip()
cost_value = int(cost_str) * float(price_str)
print(cost_value)

# Определение наиболее часто встречающихся элементов в последовательности.
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the',
         'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
         'my', 'eyes', "you're", 'under']

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
