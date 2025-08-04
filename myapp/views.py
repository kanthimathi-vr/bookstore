from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_admin_view(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        return HttpResponse("Superuser created successfully.")
    else:
        return HttpResponse("Superuser already exists.")
