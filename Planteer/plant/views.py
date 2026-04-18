from django.shortcuts import get_object_or_404, render , redirect
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

def detail_plant_view(request : HttpRequest, plant_id):

    plant = Plant.objects.get(pk=plant_id)
    return render(request, "plant/detail_plant_page.html", {"plant": plant})

def update_plant_view(request : HttpRequest, plant_id):

    plant = get_object_or_404(Plant, pk=plant_id)
    if request.method == "POST":
        plant_form = PlantForm(request.POST, request.FILES, instance=plant)
        if plant_form.is_valid():
            plant_form.save()
            return redirect('plant:plants_view')
    else:
        plant_form = PlantForm(instance=plant)
    
    return render(request, "plant/update_plant_page.html", {"plant": plant , "form": plant_form})

def delete_plant_view(request : HttpRequest, plant_id):

    plant = get_object_or_404(Plant, pk=plant_id)
    plant.delete()
    return redirect('plant:plants_view')

def search_plant_view(request : HttpRequest):

    return render(request, "plant/search_plant_page.html")

    

