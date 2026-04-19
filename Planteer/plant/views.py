from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpRequest, HttpResponse
from .models import Plant
from .forms import PlantForm
# Create your views here.
def plants_view(request : HttpRequest):
    plants = Plant.objects.all()
    search = request.GET.get('search')
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')
    if search:
        plants = plants.filter(name__icontains=search)
    if category:
        plants = plants.filter(category=category)
    if is_edible == "true":
        plants = plants.filter(is_edible=True)
    elif is_edible == "false":
        plants = plants.filter(is_edible=False)

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

    plant = get_object_or_404(Plant, pk=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(pk=plant_id)

    return render(request, "plant/detail_plant_page.html", {"plant": plant,"related_plants": related_plants})

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
    if request.method == "POST":
        plant.delete()
        return redirect('plant:plants_view')
    
    return render(request, "plant/delete_plant_page.html", {"plant": plant})
def search_plant_view(request : HttpRequest):
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        plant = Plant.objects.filter(name__contains=request.GET["search"])
    else:
        plant = []
    
    return render(request, "plant/search_plant_page.html",{"plant": plant})

