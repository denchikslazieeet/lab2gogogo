from django.shortcuts import render

# Список велосипедов в виде тестовых данных
bikes = [
    {"id": 1, "name": "Горный велосипед", "description": "Подходит для горных трасс.", "price_per_hour": 10.0},
    {"id": 2, "name": "Городской велосипед", "description": "Удобен для передвижения по городу.", "price_per_hour": 7.0},
    {"id": 3, "name": "Детский велосипед", "description": "Безопасен и легок для детей.", "price_per_hour": 5.0},
]

# Представление для главной страницы
def home(request):
    return render(request, 'rental/home.html')

# Представление для списка велосипедов
def bike_list(request):
    return render(request, 'rental/bike_list.html', {"bikes": bikes})

# Представление для деталей велосипеда
def bike_detail(request, bike_id):
    # Находим велосипед по ID или возвращаем 404
    bike = next((bike for bike in bikes if bike["id"] == bike_id), None)
    if not bike:
        return render(request, 'rental/not_found.html', status=404)
    return render(request, 'rental/bike_detail.html', {"bike": bike})

# Страницы "О нас" и "Контакты"
def about(request):
    return render(request, 'rental/about.html')

def contact(request):
    return render(request, 'rental/contact.html')
