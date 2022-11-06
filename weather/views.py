import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    key = '8c4e8b9f38faaa1ae250253e36dd4aa5'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+key

    if(request.method == "POST"):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'temp_max': res['main']['temp_max'],
            'pressure':res['main']['pressure']
        }
        all_cities.append(city_info)

    context = {"all_info": all_cities, 'form': form}
    return render(request, 'weather/index.html', context)

# Create your views here.
