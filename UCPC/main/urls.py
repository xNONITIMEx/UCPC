from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_card/', views.create, name='create_card')
]