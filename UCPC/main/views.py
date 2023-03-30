from django.shortcuts import render
from .models import Cards

def index(request):
    cards = Cards.objects.all()
    data = {
        'title': 'Главная страница',

    }
    return render(request, 'main/index.html', {'cards': cards})

def create(request):
    return render(request, 'main/create_card.html')
