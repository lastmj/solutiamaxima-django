from django.db import models

from django.contrib.auth.models import User

class PublicProblem(models.Model):
	text = models.TextField()
	javascript = models.TextField()
	title = models.CharField(max_length=255, unique=True)
	category = models.ForeignKey('publicworkspace.Categories')
	author = models.ForeignKey(User, related_name='User_authors')
	createdOn = models.DateField(auto_now_add=True)
	verifiedBy1 = models.ForeignKey(User, related_name='User_verifiedBy1s', null=True)
	verifiedBy2 = models.ForeignKey(User, related_name='User_verifiedBy2s', null=True)
	verifiedBy3 = models.ForeignKey(User, related_name='User_verifiedBy3s', null=True)
	verified = models.BooleanField(default=False)
