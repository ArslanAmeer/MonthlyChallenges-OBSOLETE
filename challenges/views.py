from django.http import HttpResponse


# Create your views here.


def index(response):
    return HttpResponse('This works!')
