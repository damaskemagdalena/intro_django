from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape


# Create your views here.

def hello(request):
    return HttpResponse("Hello, World")

def eva(request):
    return HttpResponse("Hello <span style='red'> Eva </span>")

def adam(request):
    return HttpResponse("Hello Adam")

# pobieranie do funkcji zmiennej z '' endpointu
# trzeba dodać podaną nazwe zmiennej w urls
# always remember to escape your output
def name(request, data):
    escaped_data = escape(data)
    return HttpResponse(f'Hello {escaped_data}')

def hello2(request):
    return render(request, 'hello.html')


def name2(request, data):
    return render(request, 'name.html', context={"data": data})