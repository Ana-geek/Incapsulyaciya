"""
Разработайте ĸласс Book (Книга) и реализуйте в нем
-ĸонструĸтор объеĸтов,
-набор атрибутов,
-набор аĸсессоров,
-и метод __str__().

Для тестирования данного ĸласса создайте списоĸ из
5 ĸниг различных авторов, выведите на эĸран ĸонсоли
"""


# Создаем клас с инкапсуляцией
class Books:
    def __init__(self, name: str, author: str, year: int, price: str, comment: str, rating: str):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__price = price + 'грн'
        self.__review = comment
        self.__rating = rating + ' из 10'

# Делаем метод __str__()
    def __str__(self):
        return f'{self.__name}. Автор {self.__author}, издана в {self.__year} году, цена {self.__price}. ' \
               f'Рецензия: {self.__review} {self.__rating}'

# Аксессоры
    def get_name(self) -> str:
        return self.__name

    def get_review(self) -> str:
        return self.__review


# Список моих любимых книг
b1 = Books('Гарри Поттер и кубок огня', 'Дж. К. Роулинг', 2000, '200', 'Моя любимейшая книга! Просто обожаю!', '11')
b2 = Books('Атлант расправил плечи', 'Айн Рэнд', 1959, '168', 'Шикарнейшая антиутопия', '10')
b3 = Books('Убить пересмешника', 'Ли Гарпер', 1960, '123', 'Невозможно оторваться)', '9')
b4 = Books('Шоколад', 'Джоан Гаррис', 1999, '87', 'Читала из аж слюнки текли. Но -1 за ужасную экранизацию :(', '9')
b5 = Books('Кладбище домашних животных', 'Стивен Кинг', 1983, '211',
           'До мурашек! И несмотря на, опять таки, фиговую экранизацию', '10')

# Вывод
print('====Мои любимые книги====')
print('->', b1)
print('->', b2)
print('->', b3)
print('->', b4)
print('->', b5)

print('==============Ревью===============')
print(b1.get_name(), '->', b1.get_review())
print(b2.get_name(), '->', b2.get_review())
print(b3.get_name(), '->', b3.get_review())
print(b4.get_name(), '->', b4.get_review())
print(b5.get_name(), '->', b5.get_review())

