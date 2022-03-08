# I created this whole folder, theis the same info in the iterim urls
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home.page"),
    path('services', views.services, name="int.services"),
    path('contact', views.contact, name="int.contact"),
    path('map', views.map, name="int.map"),
    path('products', views.products, name="int.products"),
]
