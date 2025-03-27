from django.db import models


class Checkbox(models.Model):
	name = models.CharField(max_length=20)
	language = models.CharField(max_length=20)
	gender = models.CharField(max_length=20,null=True,blank=True)
