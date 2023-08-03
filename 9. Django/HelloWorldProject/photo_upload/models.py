from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"title : {self.title}, image : {self.image}"