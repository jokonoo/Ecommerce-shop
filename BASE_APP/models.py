from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class News(models.Model):
	title = models.CharField(max_length = 150)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	class Meta:
		permissions = (
			('can_create_news', 'Can create news'),
			('can_update_news', 'Can update news')
			)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('website-detailnews', kwargs = {'pk': self.pk})