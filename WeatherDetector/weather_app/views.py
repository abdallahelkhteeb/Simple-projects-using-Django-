from django.shortcuts import render
import json
import urllib.request
# Create your views here.


def index(request) : 
    if request.method == 'POST' : 
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=748ecc7c3f622fe6a6a511964fa4d477').read()
        json_data = json.loads(res)
        x = float(json_data['main']['temp']) - 273.15
        data = {
            "country_code" : str(json_data['sys']['country']),
            "coordinates" : str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp' : str(x) + " C",
            'pressuer' : str(json_data['main']['pressure']),
            'humidity' : str(json_data['main']['humidity']),
            'wind_speed' : str(json_data['wind']['speed']),
        }
    else :
        city = ''
        data = {}
    return render(request, 'index.html', {'data' : data})