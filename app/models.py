from pyexpat import model
from django.db import models
from django.forms import model_to_dict

class Company(models.Model):

    name = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name =  'Company'
        verbose_name_plural =  'Companies'


