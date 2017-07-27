from django.db import models

class Dish(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	price = models.FloatField()

	def __str__(self):
		return self.name

	def toJSON(self):
		return {"dish": {"id": self.id, "name": self.name, "description": self.description, "price": self.price}}

class Order(models.Model):
	dishes = models.ManyToManyField(Dish)
	total_price = models.FloatField(default=0)
	operator = models.CharField(max_length=50)
	time = models.DateTimeField()
	restor_name = models.CharField(max_length=50)

	def __str__(self):
		return str(self.id)

	def count(self):
		if (self.total_price == 0):
			for d in self.dishes.all():
				self.total_price += d.price
		return self.total_price
