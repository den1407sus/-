from django.http import HttpResponse



def about(request):
    return HttpResponse("о сайте")


def contact(request):
    return HttpResponse("контакты")
from django.shortcuts import render
from django.shortcuts import render


def index(request):
    return render(request, "hello.html")

# Create your views here.
