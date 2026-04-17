from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant
from .forms import PlantForm
# Create your views here.
def plants_view(request : HttpRequest):
    plants = Plant.objects.all()
    return render(request, "plant/show_plant.html", {"plants": plants})

def new_plant_view(request : HttpRequest):

    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('plant:plants_view')
    else:
        plant_form = PlantForm()
        return render(request, 'plant/new_plant_page.html', {'form': plant_form})

        
    return render(request, "plant/new_plant_page.html")