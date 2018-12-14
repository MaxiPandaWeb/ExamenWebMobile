from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from .models import City
from .forms import CityForm

@login_required
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=7af76b19b340d45506f2eb4632bb2228'
    city = 'Las vegas'
    city_weather = requests.get(url.format(city)).json()
    cities = City.objects.all()

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()
    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/index.html', context)