from django.db import models

# Create your models here.
class Plant(models.Model):

    class Category(models.TextChoices):
        FRUIT = 'FRUIT','Fruit'
        VEGETABLE = 'VEGETABLE','Vegetable'
        FLOWER = 'FLOWER','Flower'
        HERB = 'HERB','Herb'
        OTHER = 'OTHER','Other'
    name = models.CharField(max_length=100)
    about  = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='images/',default='images/default.jpg')
    category = models.CharField(max_length=20,choices=Category.choices,default=Category.OTHER)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)