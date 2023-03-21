class Vacancy:
    # __slots__ = ...
    vacancy_list = []

    def __init__(self, name, url, description, salary):
        self.name = name
        self.url = url
        self.description = description
        self.salary = salary

    def __str__(self):
        return f"Назваине: {self.name}; Зарплата: {self.salary}"

    @classmethod
    def instantiate_from_api(cls, vacancy):
        cls.vacancy_list.append(vacancy)
