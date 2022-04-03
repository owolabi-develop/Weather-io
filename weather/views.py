from contextvars import Context
import json
from django.shortcuts import render
from django.template import context
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import City
from . forms import CityForm
# Create your views here.

def index(request):
    if request.method == "GET":
        form = CityForm(request.GET)
        if form.is_valid():
            CityName = form.cleaned_data['CityName']
            ApID ='9d1b46b139f8ba220cf513479b65ffd2'
            url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(CityName,ApID)
            weather = requests.get(url)
            data = json.loads(weather.text)
            url2 = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}'.format(data['coord']['lat'],data['coord']['lon'],ApID)
            weather2 = requests.get(url2)
            data2 = json.loads(weather2.text)
            weather_datas =[]
            weather_data = {
                'currentCounrty':data['sys']['country'],
                'currentName':data['name'],
                'currentTime':data2['current']['dt'],
                'currentTemp':data2['current']['temp'],
                'currentHumidity':data2['current']['humidity'],
                'currentWeatherM':data2['current']['weather'][0]['main'],
                'currentWeatherIcon':data2['current']['weather'][0]['icon'],
                'currentWeatherdesc':data2['current']['weather'][0]['description'],
                
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
                
                'dailyFeelsDay':data2['daily'][0]['feels_like']['day'],
                'dailyFeelsNight':data2['daily'][0]['feels_like']['night'],
                'dailyFeelsEve':data2['daily'][0]['feels_like']['eve'],
                'dailyFeelsMorn':data2['daily'][0]['feels_like']['morn'],
                
                'dailyWeatherIcon':data2['daily'][0]['weather'][0]['icon'],
                'dailyWeatherMain':data2['daily'][0]['weather'][0]['main'],
                'dailyWeatherDesc':data2['daily'][0]['weather'][0]['description'],
                                              
                
            }
            weather_datas.append(weather_data)
            form = CityForm()
            return render(request,'weather/index.html',{'weather':weather_datas,'form':form})
        
        

             
           
    else:
        
         form = CityForm()
        
    return render(request,'weather/index.html',{'form':form})