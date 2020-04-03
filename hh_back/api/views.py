from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company, Vacancy

# company functions
def company_list(request):
    try:
        companies = Company.objects.all()
        companies_json = [c.to_json() for c in companies]
        return JsonResponse(companies_json, safe=False)
    except:
        return JsonResponse({ "error": "Something gone wrong while reading the database..." })

def company_detailed(request, id):
    try:
        company = Company.objects.get(id=id)
        return JsonResponse(company.to_json(), safe=False)
    except:
        return JsonResponse({ "error": "Something gone wrong while reading the database..." })
    
def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
        vacancies = company.vacancy_set.all()
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except:
        return JsonResponse({ "error": "Something gone wrong while reading the database..." })


# vacancy functions:
def vacancy_list(request):
    try:
        vacancies = Vacancy.objects.all()
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except:
        return JsonResponse({ "error": "Something gone wrong while reading the database..." })

def vacancy_detailed(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        return JsonResponse(vacancy.to_json(), safe=False)
    except:
        return JsonResponse({ "error": "Something gone wrong while reading the database..." })

def top_salaries(request):
    try:
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except:
        return JsonResponse({ "error": "Something gone wrong while reading the database..." })
            