from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=512)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=1024)
	stock = models.PositiveIntegerField()
	categories = models.ManyToManyField(Category, blank=True)

	def __str__(self):
		return self.name