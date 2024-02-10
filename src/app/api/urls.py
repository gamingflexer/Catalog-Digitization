from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalouge_page, name='index'),
    path('product', views.single_product, name='index'),
]