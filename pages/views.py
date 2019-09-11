from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def greeting(request, name):
    context = {'name': name}
    return render(request, 'greeting.html', context)