from django.db import models

# Create your models here.

class Query_Storage(models.Model):
	question=models.TextField()
	answer=models.TextField()
	def __str__(self):
		return self.question[:50]
