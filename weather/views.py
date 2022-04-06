from contextvars import Context
import io
import json
from django.shortcuts import render
from django.template import context
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import City
from . forms import CityForm
# Create your views here.
from weather_io.settings import Ap_ID

def urlCall(request,CityName,ApID):
    weather_datas = []
    ApID = Ap_ID
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(CityName,ApID)
    weather = requests.get(url)
    data = json.loads(weather.text)
    try:
        url2 = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}'.format(data['coord']['lat'],data['coord']['lon'],ApID)
        weather2 = requests.get(url2)
    except:
        form = CityForm()
        return render(request,'weather/index.html',{'form':form})
    data2 = json.loads(weather2.text)
     
    weather_data = {
                'currentCounrty':data['sys']['country'],
                'currentName':data['name'],
                'currentTime':data2['current']['dt'],
                'currentTemp':data2['current']['temp'],
                'currentHumidity':data2['current']['humidity'],
                'currentWeatherM':data2['current']['weather'][0]['main'],
                'currentWeatherIcon':data2['current']['weather'][0]['icon'],
                'currentWeatherdesc':data2['current']['weather'][0]['description'],
                'currentWeatherdesc':data2['current']['weather'][0]['description'],
                'currentVisibility':data2['current']['visibility']/100,
                
                'hourlydt':data2['hourly'][0]['dt'],
                'hourlyTemp':data2['hourly'][0]['temp'],
                'hourlyFl':data2['hourly'][0]['feels_like'],
                'hourlyHd':data2['hourly'][0]['humidity'],
                'hourlyCld':data2['hourly'][0]['clouds'],
                'hourlyUvi':data2['hourly'][0]['uvi'],
                'hourlyVsis':data2['hourly'][0]['visibility'],
                
                'hourlyWeatherIcon':data2['hourly'][0]['weather'][0]['icon'],
                'hourlyWeatherM':data2['hourly'][0]['weather'][0]['main'],
                'hourlyWeatherDesc':data2['hourly'][0]['weather'][0]['description'],
                
                'dailyDt':data2['daily'][0]['dt'],
                'dailySunrise':data2['daily'][0]['sunrise'], 
                'dailySunset':data2['daily'][0]['sunset'], 
                'dailyMoonset':data2['daily'][0]['moonset'],
                'dailyMoonrise':data2['daily'][0]['moonrise'],
                
                'dailytempDay':data2['daily'][0]['temp']['day'],
                'dailytempNight':data2['daily'][0]['temp']['night'],
                'dailytempEve':data2['daily'][0]['temp']['eve'],
                'dailytempMorn':data2['daily'][0]['temp']['morn'],
                'dailytempMin':data2['daily'][0]['temp']['min'],
                'dailytempMax':data2['daily'][0]['temp']['max'],
                'dailyHumidity':data2['daily'][0]['humidity'],
                'dailyPresure':data2['daily'][0]['pressure'],
                'dailyDew':data2['daily'][0]['dew_point'],
                'dailyMoon':data2['daily'][0]['moon_phase'],
                'dailyWind':data2['daily'][0]['wind_speed']%data2['daily'][0]['wind_deg'],
                
    
                'dailyFeelsDay':data2['daily'][0]['feels_like']['day'],
                'dailyFeelsNight':data2['daily'][0]['feels_like']['night'],
                'dailyFeelsEve':data2['daily'][0]['feels_like']['eve'],
                'dailyFeelsMorn':data2['daily'][0]['feels_like']['morn'],
                
                'dailyWeatherIcon':data2['daily'][0]['weather'][0]['icon'],
                'dailyWeatherMain':data2['daily'][0]['weather'][0]['main'],
                'dailyWeatherDesc':data2['daily'][0]['weather'][0]['description'],
                
                'Currentuvi':data2['daily'][0]['uvi']
                                              
                
            }
    weather_datas.append(weather_data)
            
    return weather_datas
    
def index(request):
   
    ApID = Ap_ID
    print(ApID)
    if request.method == "GET":
        form = CityForm(request.GET)
        if form.is_valid():
            CityName = form.cleaned_data['CityName']
            form = CityForm()
            return render(request,'weather/index.html',{'weather': urlCall(request,CityName,ApID),'form':form})      
    else: 
        form = CityForm()
        
    return render(request,'weather/index.html',{'weather': urlCall(request,City.objects.all()[0],ApID),'form':form})