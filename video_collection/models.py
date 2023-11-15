from django.db import models

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=200)#constraint
    url = models.CharField(max_length=400)#constraint
    notes = models.TextField(blank=True, null=True)#notes not required

    def __str__(self):
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Notes: {self.notes[:200]}'#not showen to user, but in console IIRC?
















