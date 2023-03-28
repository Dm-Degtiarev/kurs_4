import requests
import json
import time
from classes.engine import HH
from classes.jobs import Vacancy
from classes.connector import Connector
from utils import top_10_vacancies


def main():
    page = 0

    for cicles in range(10):

        for vacancy in HH().get_request(page, 'Python')['items']:
            Vacancy.instantiate_from_api(Vacancy(
                vacancy['name'],
                vacancy['alternate_url'],
                vacancy['snippet']['responsibility'],
                vacancy['salary']
                )
            )
        page += 1


    Vacancy.save_to_json()

    z = HH().get_connector().select()

    print(top_10_vacancies(z))
