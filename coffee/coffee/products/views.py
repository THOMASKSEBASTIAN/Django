from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee

# Create your views here.


def index(request):
    dict_docs = {
        'coffee1': Coffee.objects.all()
    }
    return render(request, 'coffee.html', dict_docs)