import requests
import json
import time
from classes.engine import HH
from classes.jobs import Vacancy
from classes.connector import Connector






#!!!  Придумать как обрабатывать ошибки. Пока костыль!!!

# for cicles in range(1):
#     try:
#         for vacancy in HH().get_request(page)['items']:
#             Vacancy.instantiate_from_api(Vacancy(
#                 vacancy['name'],
#                 vacancy['alternate_url'],
#                 vacancy['snippet']['responsibility'],
#                 Vacancy.salary_reformat(vacancy['salary']['from'], vacancy['salary']['to'])
#                 )
#             )
#
#
#         page += 1
#
#     except TypeError:
#         continue
    # except KeyError:
    #     continue


# for i in Vacancy.vacancy_list:
#     print(i)
# print(len(Vacancy.vacancy_list))

# Vacancy.save_to_json()

page = 0

for cicles in range(1):

    for vacancy in HH().get_request(page, 'Python')['items']:
        Vacancy.instantiate_from_api(Vacancy(
            vacancy['name'],
            vacancy['alternate_url'],
            vacancy['snippet']['responsibility'],
            vacancy['salary']
            # Vacancy.salary_reformat(vacancy['salary']['from'], vacancy['salary']['to'])
            )
        )
    page += 1




Vacancy.save_to_json()

x = HH()


z = x.get_connector('111')

print(z.select())


