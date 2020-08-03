from django.shortcuts import render
from django.http import	HttpResponse
from .models import Task
from .forms import *


# Create your views here.
def index(request):
	form=TaskForm()

	if request.method=="POST":
		form=TaskForm(request.POST)
		print("post message received")
		if form.is_valid():

			form.save()
			print("form is saves")
			form=TaskForm()

	context={
	'title':"weather app ",
	'form'	:form


	}
	return render(request,'weather/index.html',context)

