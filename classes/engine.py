import requests
from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass


class HH(Engine):

    @staticmethod
    def inp_vacancy_list(*args):
        return ' OR '.join(args)

    def get_request(self, page_number, *vacancies):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
        par = {'per_page': '1', 'page': page_number, 'text': self.inp_vacancy_list(*vacancies)}
        response = requests.get('https://api.hh.ru/vacancies', params=par, headers=headers).json()
        return response



class SuperJob(Engine):
    def get_request(self):
        pass



# x = HH()
# print(x.get_request(5, 'Python-developer', 'Python developer'))

