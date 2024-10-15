from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'home.html')


def name(request):
    return HttpResponse("<h2>Юдин Алексей</h2>")


def age(request):
    return HttpResponse("<h2>20 лет</h2>")


def groupe(request):
    return HttpResponse("<h2>БИН-22-2</h2>")


def common(request):
    return HttpResponse("<h2>Юдин Алексей, 20 лет, БИН-22-2</h2>")
