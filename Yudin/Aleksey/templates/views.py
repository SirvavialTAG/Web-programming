from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home.html')


def name(request):
    return render(request, 'name.html')


def age(request):
    return render(request, 'age.html')


def groupe(request):
    return render(request, 'groupe.html')


def common(request):
    return render(request, 'common.html')
