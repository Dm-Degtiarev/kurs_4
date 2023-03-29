import requests
import json
from abc import ABC, abstractmethod
from classes.connector import Connector


class Engine(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_request(self):
        """Абстракция: get-запрос"""
        pass

    @staticmethod
    def get_connector(file_name='vacancies.json'):
        """ Возвращает экземпляр класса Connector """
        connector = Connector()
        connector.data_file = file_name
        return connector


class HH(Engine):
    """Класс работы с api HH"""
    @staticmethod
    def inp_vacancy_list(vacancies):
        """Приводит к нужному формату для api, для поиска по нескольким вводным"""
        return vacancies.replace(',', ' OR')

    def get_request(self, page_number, vacancies):
        """get-запрос к api HH"""
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
        par = {'per_page': '100', 'page': page_number, 'text': self.inp_vacancy_list(vacancies)}
        response = requests.get('https://api.hh.ru/vacancies', params=par, headers=headers).json()
        return response


class SuperJob(Engine):
    """Класс работы с api SuperJob"""
    def get_request(self, page_number, vacancies):
        api_key = os.getenv('SJ_API_KEY')
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
                   'X-Api-App-Id': api_key
                   }
        par = {'keywords': vacancies, 'page': page_number, 'count': 100}
        response = requests.get('https://api.superjob.ru/2.0/vacancies/search', params=par, headers=headers).json()
        return response