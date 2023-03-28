import json


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
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


