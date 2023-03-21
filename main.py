import requests
import json
import time
from classes.engine import HH
from classes.jobs import Vacancy


page = 0

for cicles in range(10):
    for vacancy in HH().get_request(page, 'Python')['items']:
        Vacancy.instantiate_from_api(Vacancy(
            vacancy['name'],
            vacancy['alternate_url'],
            vacancy['snippet']['responsibility'],
            f"{vacancy['salary']['from']} - {vacancy['salary']['to']}"
            )
        )


        page += 1


for i in Vacancy.vacancy_list:
    print(i)






