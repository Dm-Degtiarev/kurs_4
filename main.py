from utils import *
from classes.connector import Connector
# from classes.engine import Engine


def mypy():
    """
    Представляет пользователю выбрать сервис поиска вакансий;
    Формирует файл с вакансиями по заданным от пользователя ключевым словам;
    Выводит в консоль 10 самых высокооплачиваемых вакансий из списка;
    Возвращает список из 10 высокооплачиваемых вакансий.
    """
    inp_service = int(input('Добрый день! Выберите сервис: HH - введите 1, SuperJob - введите 2\n'))
    if inp_service not in (1, 2):
        print('Введено некорректное значение. Повторите ввод сначала')
        mypy()
    inp_keywords = str(input('Введите, через заяптую, ключевые слова по которым будет проходить поиск вакансий\n' ))

    if inp_service == 1:
        print('10 самых высокооплачиваемых вакансий по запросу: ')
        hh(inp_keywords)
        print('Файл vacancies.json создан!')
    elif inp_service == 2:
        print('Загружаю 10 самых высокооплачиваемых вакансий по запросу: ')
        super_job(inp_keywords)
        print('Файл vacancy.json создан!')
    else:
        print('Произошла ошибка. Закрытие программы ...')

    inp_agreement = int(input('\nВы хотите выполнить поиск вакансий по заданному слову? Если да введите - 1, если нет - 0\n'))
    if inp_agreement == 1:
        inp_attr = int(input('По какому атрибуту вы хотите произвести поиск? Введите: 1 - vacancy_name, 2 - vacancy_url, '
                             '3 - vacancy_info, 4 - vacancy_salary\n'))
        inp_keyword = str(input('Введите ключевое слово поиска:\n'))
        vacancy_attr = return_vacancy_attr(inp_attr)

        x = HH().get_connector().sorted(vacancy_attr, inp_keyword)
        vacancy_list_reformat(x)

    else:
        pass


if __name__ == '__main__':
    mypy()
