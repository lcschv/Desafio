from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.URLField(max_length=200)


class Servers(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	cpu = models.CharField(max_length=200)
	memoria = models.IntegerField(default=0)
	disco = models.IntegerField(default=0)
	os = models.CharField(max_length=200)
	descricao = models.CharField(max_length=500)
	preco = models.DecimalField(max_digits=8, decimal_places=2)
