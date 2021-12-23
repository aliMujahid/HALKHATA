from django.shortcuts import render

def home(request):
    return render(request, 'halkhata_app/home.html')
