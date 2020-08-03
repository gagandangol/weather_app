from django.shortcuts import render
from django.http import	HttpResponse
from .models import Task
from .forms import *
import requests


# Create your views here.
def index(request):
	url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=a971a09fcd0f02537230ea4564060038'
	# city='kathmandu'
	# r=requests.get(url.format(city)).json()
	#api key a971a09fcd0f02537230ea4564060038
	cities=Task.objects.all()
	#cities='api.openweathermap.org/data/2.5/weather?q={kathmandu}&appid={a971a09fcd0f02537230ea4564060038}'

	weather_data_city=[]

	for city in cities:
		try:
			r=requests.get(url.format(city)).json()

			city_weather={
				
				'title':"weather app ",
				'cities':city,
				'temperature':round(r['main']['temp']-273,2),
				'description':r['weather'][0]['description'],
				'icon':r['weather'][0]['icon']
				}
			weather_data_city.append(city_weather)
		except:
			pass

	context={'weather_data':weather_data_city}
	return render(request,'weather/index.html',context)

# def cityAdd(request):
# 	form=TaskForm()
# 	if request.method=="POST":
# 		form=TaskForm(request.POST)
# 		print("post message received")
# 		if form.is_valid():

# 			form.save()
# 			print("form is saves")
# 			form=TaskForm()
# 	context={

	# 	'form':form
	# }

	# return render(request,'weather/index.html',context)

