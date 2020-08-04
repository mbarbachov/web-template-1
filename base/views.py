from django.shortcuts import render


def home(request):
    return render(request, 'base/mainPage.html')


def about(request):
    return render(request, 'base/template.html')


def service(request):
    return render(request, 'base/template.html')


def pricing(request):
    return render(request, 'base/template.html')


def contacts(request):
    return render(request, 'base/template.html')
