def top_10_vacancies(vacancies):
    vacancies.sort(key=lambda sort: sort['vacancy_salary'], reverse=True)
    return vacancies[0:10]


