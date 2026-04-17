from django.urls import path
from . import views
app_name = "plant"
urlpatterns = [
    path('all/', views.plants_view, name="plants_view"),
    path('new/', views.new_plant_view, name="new_plant_view"),
]