from django.db import models

# Create your models here.
class Mymodel(models.Model):
	name=models.CharField(max_length=20)
	image=models.ImageField()