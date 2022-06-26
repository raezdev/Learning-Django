from cgitb import text
from django.shortcuts import redirect, render
from django.http import HttpResponse, response

# Create your views here.

def index(request):
    return render(request, 'index.html')

def wordcounter(request):
    #texto = request.GET.get('texto')
    texto = request.POST.get('texto')
    words = len(texto.split())
    
    context = {
        'words': words
    }
    return render(request, 'wordcounter.html', context)
