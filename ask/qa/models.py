from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-id')
	
	def popular(self):
		return self.order_by('-rating')

class Question(models.Model):
	objects = QuestionManager()

	title = models.CharField(blank=True, null=True, max_length=50)
	text = models.TextField(blank=True, null=True)
	added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	rating = models.IntegerField(default=0, blank=True, null=True)
	author = models.OneToOneField(User, blank=True, null=True)
	likes = models.ManyToManyField(User, blank=True, related_name='question_like_user')

	def get_url(self):
		return '/question/'+str(self.id)

class Answer(models.Model):
	text = models.TextField(blank=True, null=True)
	added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	question = models.ForeignKey(Question, blank=True, null=True)
	author = models.ForeignKey(User, blank=True, null=True)

	
