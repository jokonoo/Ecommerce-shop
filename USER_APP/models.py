from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	nickname = models.CharField(max_length = 100)
	description = models.CharField(max_length = 500, blank = True, null = True)
	picture = models.ImageField(upload_to = 'ProfilePictures', default = 'default.jpg', null = True, blank = True)

	def __str__(self):
		return self.user.username

	def save(self, *args, **kwargs):
		super().save()
		
		img = Image.open(self.picture.path)

		if img.height > 300 or img.height < 300 or img.width > 300 or img.width < 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.picture.path)

class Comment(models.Model):
	author = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	content = models.TextField()
	date = models.DateTimeField(default = timezone.now)

class ShippingAddress(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	fullname = models.CharField(max_length = 200, null = True, blank = True)
	country = models.CharField(max_length = 200, null = True, blank = True)
	city = models.CharField(max_length = 200, null = True, blank = True)
	street = models.CharField(max_length = 200, null = True, blank = True)
	apartment = models.CharField(max_length = 200, null = True, blank = True)
	zipcode = models.CharField(max_length = 200, null = True, blank = True)
	phone = models.IntegerField(null = True, blank = True)

	def __str__(self):
		return f'ShippingAddress of {self.user.username}'


		
		