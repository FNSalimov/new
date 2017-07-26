from django.db import models

class Dish(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	price = models.FloatField()

	def __str__(self):
		return self.name

	def toJSON(self):
		return {"dish": {"id": self.id, "name": self.name, "description": self.description, "price": self.price}}