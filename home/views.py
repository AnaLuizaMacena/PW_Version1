from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index (request):
    return render (request, 'index.html')

def sobre (request):
    return HttpResponse ('<h1>Sistema 1.0 desenvolvido por mesmo<h1>')

def contato (request):
    return HttpResponse ('Esta é a pagina de contato')
