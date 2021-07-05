from django.db import models

# Create your models here.

class addQuotes(models.Model):
	quotes = models.TextField()
	author=models.CharField(max_length=100)

	def __str__(self):
		if(len(self.quotes)>50):
			return self.quotes[:50]+'...'+'('+str(self.id)+')'

		return self.quotes + '(' + str(self.id) + ')'


