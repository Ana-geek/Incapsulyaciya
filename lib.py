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
