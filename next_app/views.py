from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse("Hello, World")

def eva(request):
    return HttpResponse("Hello <span style='red'> Eva </span>")

def adam(request):
    return HttpResponse("Hello Adam")

# pobieranie do funkcji zmiennej z '' endpointu
# trzeba dodać podaną nazwe zmiennej w urls
def name(request, data):
    return HttpResponse(f'Hello {data}')