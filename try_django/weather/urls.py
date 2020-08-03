from django.urls import path
from . import views

urlpatterns = [
    # path('', views.cityAdd, name="cityAdd"),
    path('', views.index, name="index"),
    path('/weather/index', views.index, name="index"),
    # path('/weather/addcity', views.cityAdd, name="add_city")

]