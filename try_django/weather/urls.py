from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/weather/index', views.index, name="index")

]