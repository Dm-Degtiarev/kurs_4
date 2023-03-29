def top_10_vacancies(vacancies):
    vacancies.sort(key=lambda sort: sort['vacancy_salary'], reverse=True)

    index = 1
    for vacancy in vacancies[0:10]:
        print(f'{index}. {vacancy}')
        index +=1

    return vacancies[0:10]


