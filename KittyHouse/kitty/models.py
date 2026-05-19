from django.db import models

# Create your models here.
class Volunteer(models.Model):
    name = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name[:15]
    
class Cat(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='cats/', blank=True)
    description = models.TextField() 
    age = models.IntegerField()

    def __str__(self):
        return self.name