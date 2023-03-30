import json
from classes.engine import *

class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    @property
    def data_file(self):
        """геттер для data_file"""
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        """сеттер для data_file"""
        self.__data_file = value
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        try:
            with open(self.__data_file, "r", encoding='utf-8') as file:
                json.load(file)
        except FileNotFoundError:
            with open(self.__data_file, "w", encoding='utf-8') as file:
                json.dump([], file)
        except json.JSONDecodeError:
            raise Exception("Json файл поврежден")

    def select(self):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        with open(self.__data_file, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
        return existing_data

    def insert(self, value: dict):
        """
        Запись данных в файл с сохранением структуры и исходных данных;
        Если вводится пустой словарь - данные не записываются;
        Если ввоодится не словарь - программа возвращает исключение.
        """
        if value.__class__.__name__ != 'dict':
            raise "класс добавляемого объекта должен быть 'dict'"
        elif value == {}:
            pass
        else:
            with open(self.__data_file, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
            existing_data.append(value)

            with open(self.__data_file, "w", encoding='utf-8') as file:
                json.dump(existing_data, file, indent=4, ensure_ascii=False)


    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        with open(self.__data_file, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
        try:
            existing_data.remove(query)
        except ValueError:
            pass

        with open(self.__data_file, "w", encoding='utf-8') as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False)


    def sorted(self, attr, keyword):
        with open(self.__data_file, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
        vacancies = []

        for i in existing_data:
            try:
                if keyword.lower() in i[attr].lower():
                    vacancies.append(i)
                else:
                    continue
            except AttributeError:
                continue

        return vacancies


#Тест
if __name__ == '__main__':
    print(HH().get_connector().select())
    HH().get_connector().insert({"1": 1})
    HH().get_connector().insert({"2": 2})
    HH().get_connector().delete({'2': 2})
    HH().get_connector().insert(1)
