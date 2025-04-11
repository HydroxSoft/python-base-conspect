# Три основных принципа объектно-ориентированного программирования (ООП) на одном примере:

# Инкапсуляция: Инкапсуляция данных и методы внутри классов, таких как Profession, где атрибуты __profession_name
# и __salary скрыты от прямого доступа и доступны только через методы (get_profession(), get_salary()).

# Наследование: Использование наследования, создав классы Nationality, Russian, English, Chinese,
# которые наследуют атрибуты и методы от класса Person.
# Это позволяет повторно использовать код и добавлять специфические для каждого подкласса методы.

# Полиморфизм: Использование полиморфизма с помощью метода talks(), который реализован
# по-разному в классах Russian, English, Chinese.
# Это вызывает метод talks() для объектов разных классов и получать разные результаты.

# Для работы с абстрактными классами в Python используется модуль abc.
# ABC: Базовый класс для создания абстрактных классов.
# abstractmethod: Декоратор указывает, что метод является абстрактным и должен быть реализован в подклассах.
from abc import ABC, abstractmethod


# Использование декоратора или проверки типа: Вы можете написать декоратор или проверку внутри метода,
# чтобы он работал только для экземпляров класса Person, но не для его наследников.
def check_person(func):
    def wrapper(self, *args, **kwargs):
        if type(self) is not Person:
            raise AttributeError("This method is only available for the Person class.")
        return func(self, *args, **kwargs)

    return wrapper


# Создание класса на примере персоны.
class Person:
    # Инициализация класса Person.
    def __init__(self, name, second_name, age):
        self.name = name
        self.second_name = second_name
        self.age = age

    # Возвращает строковое представление объекта Person.
    def __str__(self):
        return f"{self.name} {self.second_name}, Age: {self.age}"

    # Функция greet является методом класса Person так как определена внутри него
    # и связана с объектом этого класса.
    def speak(self):
        return f", my name is {self.name} and I am {self.age} years old."

    # Функция принадлежащая исключительно клаccу Person.
    @check_person
    def greeting(self):
        print(f"My name is {self.name} and I am base class present.")

    # Функция greet создает обязательный интерфейс для всех подклассов, требуя реализации метода greet().
    # Выбрасывает NotImplementedError, если метод не переопределен в подклассе.
    def greet(self):
        raise NotImplementedError("The method must be overridden in a subclass.")


# Наследование классов.
# В Python поддерживается наследование, где один класс может наследовать свойства и методы другого.
# Если параметры конструктора полностью идентичны родительским, можно опустить явное определение __init__:
# Или родительский конструктор используется по умолчанию если параметры указаны в первом классе.
class Nationality(Person):
    # Словарь для сопоставления национальностей с приветствиями
    greetings = {"russian": "Privet", "english": "Hello", "chinese": "Nihao"}

    # Наследники должны передавать все необходимые параметры в родительский класс через super()
    def __init__(self, name, second_name, age, profession, salary, nationality):
        # Явная передача всех параметров
        super().__init__(name, second_name, age)
        # Новый атрибут
        self.profession = profession
        self.salary = salary
        self.nationality = nationality

    def greet(self):
        if self.nationality in self.greetings:
            return f"{self.name} {self.second_name} say: {self.greetings[self.nationality]}{self.speak()}"
        else:
            return f"I am {self.nationality} and i dont have greetings."


class Russian(Nationality):
    # Наследники должны передавать все необходимые параметры в родительский класс через super()
    def __init__(self, name, second_name="", age=0, profession="", salary=0):
        # Явная передача всех параметров
        super().__init__(name, second_name, age, profession, salary, nationality="russian")

    def asked(self):
        return f" I am {self.nationality}. I work {self.profession} with salary {self.salary} dollars."

    def talks(self):
        return self.greet() + self.speak() + self.asked()


class English(Nationality):
    def __init__(self, name, second_name="", age=0, profession="", salary=0):
        # Обязательный вызов родительского конструктора
        super().__init__(name, second_name, age, profession, salary, nationality="english")

    def asked(self):
        return f" I am {self.nationality}. I work {self.profession} with salary {self.salary} dollars."

    def talks(self):
        return self.greet() + self.speak() + self.asked()


class Chinese(Nationality):
    def __init__(self, name, second_name="", age=0, profession="", salary=0):
        # Полная инициализация родительского класса
        super().__init__(name, second_name, age, profession, salary, nationality="chinese")

    def asked(self):
        return f" I am {self.nationality}. I work {self.profession} with salary {self.salary} dollars."

    def talks(self):
        return self.greet() + self.speak() + self.asked()


# Инкапсуляция и методы доступа
# Инкапсуляция скрывает данные от внешнего мира и позволяет взаимодействовать с ними через методы доступа.
class Profession:
    def __init__(self, profession_name, salary):
        # Приватный атрибут
        self.__profession_name = profession_name
        # Приватный атрибут
        self.__salary = salary

    # Методы доступа для получения информации о профессии
    def get_profession(self):
        return self.__profession_name

    def get_salary(self):
        return self.__salary

    # Методы доступа для изменения информации о профессии
    def set_profession_name(self, profession_name):
        self.__profession_name = profession_name

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            raise ValueError("Salary cannot be negative")


# Создание объекта Person
greeting_person = Person("Jack", "Winston", 30)
greeting_person.greeting()

# Полноценная реализация всех наследников.
profession_one = Profession("software engineer", 50000)
profession_two = Profession("school teacher", 40000)
profession_tree = Profession("policeman", 30000)

profs = [profession_one.get_profession(), profession_two.get_profession(), profession_tree.get_profession()]
salaries = [profession_one.get_salary(), profession_two.get_salary(), profession_tree.get_salary()]

person_one = Russian("Viktor", "Belov", 20, profs[0], salaries[0])
person_two = English("John", "Kameron", 25, profs[1], salaries[1])
person_tree = Chinese("Chen", "Ming", 35, profs[2], salaries[2])

# Полиморфизм
# Полиморфизм позволяет использовать объекты разных классов через общий интерфейс.
# Это способность объектов разных классов реагировать по-разному на один и тот же метод на примере talks().
people = [person_one, person_two, person_tree]
for person in people:
    print(person.talks())

# Класс object() в Python, возвращает безликий объект, возвращает
# новый безликий объект и является базой для всех классов.
obj = object()
print('object: ', type(obj))

# Функция isinstance() в Python, принадлежность экземпляра к классу, вернет True,
# если проверяемый объект является экземпляром указанного класса (классов), или прямым,
# косвенным или виртуальным подклассом от него.
print('isinstance: ', isinstance(person_one, Person))

# Функция issubclass() в Python, проверяет наследование класса, возвращает True, если указанный класс
# является подклассом (прямым, косвенным или виртуальным) указанного класса (классов).
print('issubclass: ', issubclass(Russian, Person))

# Функция getattr() в Python, значение атрибута по имени возвращает значение
# атрибута указанного объекта по его имени.
print('getattr: ', getattr(person_one, 'name'))

# Функция hasattr() в Python, наличие атрибута объекта, проверяет существование атрибута в указанном объекте.
# Возвращает True, если атрибут с таким именем существует, иначе False.
print('hasattr: ', hasattr(person_one, 'name'))

# Функция setattr() в Python, создает атрибут объекта, устанавливает
# значение атрибута указанного объекта по его имени.
setattr(person_one, 'name', 'Ivan')
print('setattr: ', person_one.name)

# Функция delattr() в Python, удаляет атрибут объекта, удаляет из объекта указанный атрибут, если объект
# позволяет это сделать.
deleted_attr = person_one.name
delattr(person_one, 'name')
try:
    print('delattr: ', person_one.name)
except AttributeError:
    print('delattr: ', 'Attribute ', deleted_attr, ' deleted')


# Класс classmethod в Python, делает функцию методом класса. Делает указанную функцию методом класса.
# Метод класса может быть вызван либо для класса (например, C.f()), либо для экземпляра (например, C().f()).


class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


obj1 = MyClass()
obj2 = MyClass()
print('classmethod: ', MyClass.get_count())


# Декоратор staticmethod() в Python, метод класса в статический метод, преобразует метод класса в
# статический метод этого класса.


class MyStaticClass:
    @staticmethod
    def my_static_method():
        return "This is a static method."


print('staticmethod: ', MyStaticClass.my_static_method())


# Класс property() в Python, метод класса как свойство, позволяет использовать методы в качестве
# вычисляемых свойств объектов (дескрипторов данных).


class MyPropertyClass:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


obj3 = MyPropertyClass("John")
print('property one: ', obj3.name)
obj3.name = "Jane"
print('property two: ', obj3.name)


# Функция repr() в Python, описание объекта, вернет строку, содержащую
# печатаемое формальное представление объекта.


class MyReprClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"MyReprClass('{self.name}')"


obj4 = MyReprClass("Doe")
print('repr: ', repr(obj4))

# Функция super() в Python, доступ к унаследованным методам, возвращает объект объект-посредник, который
# делегирует вызовы метода родительскому или родственному классу, указанного типа.
# Это полезно для доступа к унаследованным методам, которые были переопределены в классе.
print('super: ')


class ParentClass:
    def greet(self):
        print("super parent: Hello from Parent")


class ChildClass(ParentClass):
    def greet(self):
        super().greet()
        print("super child: Hello from Child")


child = ChildClass()
child.greet()

# Функция vars() в Python, словарь переменных объекта, вернет атрибут __dict__ - словарь пространства
# имен для модуля, класса, экземпляра или любого другого объекта с атрибутом __dict__.
print('vars: ', vars(person_one))


# Абстрактные классы
# Абстрактные классы в Python — это фундаментальная концепция объектно-ориентированного программирования (ООП),
# которая позволяет создавать базовые классы, которые не могут быть инстанцированы самостоятельно.
# Они служат основой для других классов, предоставляя общую структуру и функциональность,
# которую наследники могут расширять и реализовывать по-своему.
# Абстрактный класс — это класс, который не может быть создан как объект напрямую.
# Его основная цель — служить базовым классом для других классов, определяя общие свойства и методы,
# которые будут реализованы в наследниках.
# Абстрактные методы — это методы внутри абстрактного класса, которые не имеют реализации.
# Они определяют поведение, которое должно быть реализовано в каждом подклассе.

# Различия с Обычными Классами
# Экземпляры: Обычные классы можно инстанцировать напрямую, тогда как абстрактные классы — нет.
# Наследование: Обычные классы могут быть использованы как самостоятельные классы,
# тогда как абстрактные классы предназначены для наследования.

class Game(ABC):
    def __init__(self, name):
        self.name = name

    # Декоратор @abstractmethod из модуля abc используется для обозначения метода как абстрактного.
    @abstractmethod
    def play(self):
        pass

    def display_info(self):
        print(f"Game: {self.name}")


# Подклассы
class Chess(Game):
    def __init__(self):
        super().__init__("Chess")

    def play(self):
        print("Playing Chess...")


class Checkers(Game):
    def __init__(self):
        super().__init__("Checkers")

    def play(self):
        print("Playing Checkers...")


class VideoGame(Game):
    def __init__(self, game_name):
        super().__init__(game_name)

    def play(self):
        print(f"Playing {self.name}. Controlling the character...")


# Создание экземпляров игр
chess = Chess()
checkers = Checkers()
video_game = VideoGame("The Last of Us")


# Добавление метода вывода информации и запуск игр.
def start_game(game: Game):
    game.display_info()
    game.play()


# Использование
start_game(chess)
start_game(checkers)
start_game(video_game)


# Метаклассы
# Метаклассы - позволяют создавать классы, которые определяют поведение и свойства других классов.
# По сути, метакласс - это класс, экземпляры которого являются классами.
# В Python все классы создаются с помощью метакласса type, который является базовым метаклассом по умолчанию.

# Метакласс — это класс, который отвечает за создание других классов.
# Он позволяет контролировать процесс создания, изменения и удаления классов и их атрибутов.
# Метаклассы часто используются для добавления дополнительной функциональности или контроля над классами.


# Создание метакласса и реализация его методов.
class MyMeta(type):
    # __new__: Этот метод вызывается при создании нового класса. Он принимает четыре аргумента:
    # cls (ссылка на метакласс), name (имя создаваемого класса),
    # bases (кортеж родительских классов) и dct (словарь атрибутов класса).
    def __new__(cls, name, bases, dct):
        print(f"Creating a new class {name}")
        # Добавление нового атрибута к классу
        dct['new_attr'] = "This is a new attribute."
        return super().__new__(cls, name, bases, dct)

    # __init__: Этот метод вызывается после создания класса.
    # Он используется для инициализации атрибутов метакласса.
    def __init__(cls, name, bases, dct):
        print(f"Initializing a class {name}")
        super().__init__(name, bases, dct)

    # __call__: Этот метод вызывается при создании экземпляра класса.
    # Он может быть переопределен для изменения поведения при создании объектов.
    def __call__(cls, *args, **kwargs):
        print(f"Creating an instance of a class {cls.__name__}")
        instance = super().__call__(*args, **kwargs)
        # Добавление нового атрибута к экземпляру
        instance.new_instance_attr = "This is a new instance attribute."
        return instance


class MyClass(metaclass=MyMeta):
    def __init__(self, value):
        self.value = value


# Создание экземпляра MyClass
obj = MyClass("created аttribute")

# Вывод атрибутов с помощью getattr()
print(getattr(MyClass, 'new_attr', "Attribute not found"))
print(getattr(obj, 'new_attr', "Attribute not found"))
print(getattr(obj, 'new_instance_attr', "Attribute not found"))
print(getattr(obj, 'value', "Attribute not found"))


# Дескрипторы в Python — это объекты, которые реализуют один или несколько специальных методов:
# __get__(self, instance, owner): Этот метод вызывается при попытке получить значение атрибута.
# Он позволяет реализовать логику для чтения атрибута.
# __set__(self, instance, value): Этот метод вызывается при попытке изменить значение атрибута.
# Он позволяет реализовать логику для записи атрибута, например, валидацию данных.
# __delete__(self, instance): Этот метод вызывается при попытке удалить атрибут.
# Он позволяет реализовать логику для удаления атрибута.
# Они позволяют управлять доступом к атрибутам класса и определять дополнительное поведение
# при их получении, изменении или удалении.

# Пример Дескриптора для Валидации Данных
class PositiveNumber:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"Value must be positive")
        instance.__dict__[self.name] = value


class NumberClass:
    attr = PositiveNumber('attr')


obj = NumberClass()
obj.attr = 5
print(obj.attr)

try:
    obj.attr = -3
except ValueError as e:
    print(e)
