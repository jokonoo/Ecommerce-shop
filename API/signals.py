from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender = User)
def admin_token_creation(sender, instance, created, **kwargs):
	if created:
		if instance.is_staff == True:
			Token.objects.create(user=instance)

