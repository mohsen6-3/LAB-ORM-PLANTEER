from django.contrib import admin
from .models import Plant, Comment ,Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'flag')

class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_edible', 'created_at')
    list_filter = ('category', 'is_edible')
    search_fields = ('name', 'about', 'used_for')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'plant', 'created_at')
    list_filter = ('plant', 'created_at')
    search_fields = ('name', 'comment')


# Register your models here.
admin.site.register(Plant, PlantAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Country, CountryAdmin)
