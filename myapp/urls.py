from django.urls import path
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Welcome to the Bookstore!")

urlpatterns = [
    path('', homepage),
]
