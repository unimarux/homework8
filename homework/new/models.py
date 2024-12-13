from django.db import models

class Type (models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Flower (models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Type,on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)
    summary = models.TextField(blank=True,null=True)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title
