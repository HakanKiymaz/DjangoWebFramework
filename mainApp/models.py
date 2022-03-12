from django.db import models

from django.contrib.auth.models import User
# Create your models here.
"""
Models are blueprint for Database.
It's a template of how we are going to store data for this app
"""
class ToDoList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=250)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.text