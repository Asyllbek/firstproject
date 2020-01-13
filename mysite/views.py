from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def generic(request):
    return render(request, 'generic.html', {})

