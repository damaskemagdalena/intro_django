from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello, world")

# zrobić endpoint, gdzie wyswietli się przywitanie z imieniem w kolorze czerwonym
def hello_you(request):
    return HttpResponse("<h2>Hello, <span style='color:red'>Madziunia!</span></h2>")

def hi(request):
    return HttpResponse("""<!DOCTYPE html> 
    <html>
        <head>
            <meta charset='UTF-8'>
            <title>Hi</title>
        </head>
        <body>Hi, world</body>
    </html>""")


# przekazanie kodu html za pomocą szablonu z pliku templates
def hi2(request):
    return render(request, 'hi.html')