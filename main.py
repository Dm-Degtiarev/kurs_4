import requests
import json
import time
from classes.engine import HH
from classes.jobs import Vacancy



page = 0

#!!!  Придумать как обрабатывать ошибки. Пока костыль!!!
for cicles in range(10):
    for vacancy in HH().get_request(page, 'Python')['items']:

        try:
            Vacancy.instantiate_from_api(Vacancy(
                vacancy['name'],
                vacancy['alternate_url'],
                vacancy['snippet']['responsibility'],
                Vacancy.salary_reformat(vacancy['salary']['from'], vacancy['salary']['to'])
                )
            )
        except TypeError:
            continue

        page += 1


Vacancy.create_dict()


