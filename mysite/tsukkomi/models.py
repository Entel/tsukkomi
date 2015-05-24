from django.db import models

# Create your models here.
class Content(models.Model):
	text = models.CharField(max_length=280)
	ip = models.CharField(max_length=100)
	time = models.DateTimeField('date publish')
	def __unicode__(self):
		return self.text

class Rate(models.Model):
	content = models.ForeignKey(Content) 
	up = models.IntegerField()
	ip = models.CharField(max_length=100)
	time = models.DateTimeField('date publish')
	def __unicode__(self):
		return self.up

class Comment(models.Model):
	content = models.ForeignKey(Content) 
	text = models.CharField(max_length=280)
	ip = models.CharField(max_length=100)
	time = models.DateTimeField('date publish')
	def __unicode__(self):
		return self.text
