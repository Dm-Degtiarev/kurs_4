import json


class Vacancy:
    """Вакансии (общее)"""
    __slots__ = ('name', 'url', 'description', 'salary')
    vacancy_list = []

    def __init__(self, name='NULL', url='NULL', description='NULL', salary='NULL'):
        """Инициализация: наим. вакансии, url, описание, ЗП"""
        self.name = name
        self.url = url
        self.description = description
        self.salary = salary

    def __str__(self):
        """Выводит инфо о объекте класс в формате: Название вакакнсии, Зарплата"""
        return f"Название: {self.name}; Зарплата: {self.salary}"

    def __repr__(self):
        """Выводит инфо о объекте класс в формате: Название вакакнсии, Зарплата (тех.)"""
        return f"Название: {self.name}; Зарплата: {self.salary}"

    @classmethod
    def instantiate_from_api(cls, vacancy):
        """Добавляет объект в список объектов класса"""
        cls.vacancy_list.append(vacancy)


    @classmethod
    def save_to_json(cls, path='vacancies'):
        """Создает JSON на основе списка объекетов текущего класса"""
        vacansy_json = []

        for i in cls.vacancy_list:
            vacansy_json.append(
                {
                    "vacancy_name": i.name,
                    "vacancy_url": i.url,
                    "vacancy_info": i.description,
                    "vacancy_salary": i.salary
                }
            )

        with open(f"{path}.json", "w", encoding='utf-8') as file:
            file.write(json.dumps(vacansy_json, indent=4, ensure_ascii=False))


class HHVacancy(Vacancy):
    """Вакансии HH"""
    __slots__ = Vacancy.__slots__

    @staticmethod
    def salary_reformat(salary):
        """
        Возвращет: если ЗП не указана - NULL,
        если есть макс. зарплата - максимальная заррплата
        если нет макс. зарплаты - минимальная зарплата
        """
        if salary is None:
            return 0
        elif salary['to'] is not None:
            return salary['to']
        else:
            return salary['from']

    @classmethod
    def save_to_json(cls, path='vacancies'):
        """Создает JSON на основе списка объекетов текущего класса"""
        vacansy_json = []

        for i in cls.vacancy_list:
            vacansy_json.append(
                {
                    "vacancy_name": i.name,
                    "vacancy_url": i.url,
                    "vacancy_info": i.description,
                    "vacancy_salary": cls.salary_reformat(i.salary)
                }
            )

        with open(f"{path}.json", "w", encoding='utf-8') as file:
            file.write(json.dumps(vacansy_json, indent=4, ensure_ascii=False))


class SJVacancy(Vacancy):
    """Вакансии SuperJob"""
    __slots__ = Vacancy.__slots__






        



