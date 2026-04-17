from django.http import HttpResponse


def index(request):
    return HttpResponse("главная")


def about(request):
    return HttpResponse("о сайте")


def contact(request):
    return HttpResponse("контакты")
