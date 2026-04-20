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

    def __str__(self):
        return self.name

class Comment(models.Model):
    plant =models.ForeignKey(Plant,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.plant.name}"
    