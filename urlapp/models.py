from django.db import models

# Create your models here.
class UrlData(models.Model):
    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=20)

def __str__(self):
    return f'short Url for: {self.url} is: {self.slug}'
 
