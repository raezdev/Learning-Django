from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hola, Bienvenido</h1>')

    context = {
         'name': 'Ráez',
         'age': 37,
         'pais': 'Spain'
    }
    return render(request, 'index.html', context)

