from django.db import models

class Categories(models.Model):
	title = models.CharField(max_length=255)
	parentCategory = models.ForeignKey('Categories', blank=True, null=True)
	position = models.IntegerField(default=0)
	activated = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.title
