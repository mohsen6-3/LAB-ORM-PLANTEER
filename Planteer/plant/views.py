from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def plants_view(request : HttpRequest):
    return render(request, "plant/show_plant.html")