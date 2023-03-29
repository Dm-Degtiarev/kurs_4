import requests
import json
import time
from classes.engine import HH, SuperJob
from classes.jobs import HHVacancy, SJVacancy
from classes.connector import Connector


def top_10_vacancies(vacancies):
    """Возвращает 10 самых высокооплачиваемых вакансий а так же выводит их в консоль"""
    vacancies.sort(key=lambda sort: sort['vacancy_salary'], reverse=True)

    index = 1
    for vacancy in vacancies[0:10]:
        print(f"""\n---{index}---
        Наименование вакансии: {vacancy['vacancy_name']}
        URL вакансии: {vacancy['vacancy_url']}
        Описание вакансии: {vacancy['vacancy_info']}
        Зарплата: {vacancy['vacancy_salary']}""")

        index +=1

    return vacancies[0:10]

def hh(vacancies):
    """
    HH. Создает JSON c 1000 вакасиями по ключевым словам в *args, а так же
    выводит в консоль 10 самых выскоооплачиваемых вакансий из этого файла
    """
    key_words = HH.inp_vacancy_list(vacancies)
    page = 0

    for cicles in range(10):
        hh_request = HH().get_request(page, key_words)['items']
        for vacancy in hh_request:
            HHVacancy.instantiate_from_api(HHVacancy(
                vacancy['name'],
                vacancy['alternate_url'],
                vacancy['snippet']['responsibility'],
                vacancy['salary']
                )
            )
        page += 1

    HHVacancy.save_to_json('vacancies')
    z = HH().get_connector().select()
    top_10_vacancies(z)

def super_job(vacancies):
    """
    SuperJob. Создает JSON c 1000 вакасиями по ключевым словам в *args, а так же
    выводит в консоль 10 самых выскоооплачиваемых вакансий из этого файла
    """
    key_words = vacancies
    page = 0

    for cicles in range(10):
        sj_request = SuperJob().get_request(page, key_words)['objects']
        for vacancy in sj_request:
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
