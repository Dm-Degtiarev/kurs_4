import requests
import json
import time
from classes.engine import HH, SuperJob
from classes.jobs import HHVacancy, SJVacancy
from classes.connector import Connector
from utils import top_10_vacancies


def hh():
    page = 0

    for cicles in range(10):

        for vacancy in HH().get_request(page, 'Python')['items']:
            HHVacancy.instantiate_from_api(HHVacancy(
                vacancy['name'],
                vacancy['alternate_url'],
                vacancy['snippet']['responsibility'],
                vacancy['salary']
                )
            )
        page += 1


    HHVacancy.save_to_json('HH_vacancies')
    z = HH().get_connector().select()
    print(top_10_vacancies(z))


def super_job():
    page = 0
    for cicles in range(10):
        for vacancy in SuperJob().get_request(page, 'Python', 'C++')['objects']:
            SJVacancy.instantiate_from_api(SJVacancy(
                vacancy['profession'],
                vacancy['link'],
                vacancy['vacancyRichText'],
                vacancy['payment_to']
                )
            )
        page += 1

    SJVacancy.save_to_json('vacancies')
    z = SuperJob().get_connector().select()
    top_10_vacancies(z)

# hh()
super_job()
# if __name__ == '__main__':
#     main()
