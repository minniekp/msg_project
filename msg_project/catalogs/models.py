# catalogs/models.py 
from django.conf import settings 
from django.db import models 
from django.urls import reverse

class Catalog(models.Model): 
    DatasetName = models.CharField(max_length=280)
    Type = models.CharField(max_length=280)
    Classification = models.CharField(max_length=280)
    OriginalSource = models.CharField(max_length=280)
    OriginalOwner = models.CharField(max_length=280)
    YearofOrigin = models.DateTimeField(auto_now_add=True) 
    
    def get_absolute_url(self): 
        return reverse('catalog_detail', args=[str(self.id)])

    def __str__(self): 
        return self.DatasetName
