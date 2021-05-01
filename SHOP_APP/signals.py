from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Shipping

@receiver(post_save, sender = Order)
def shipping_instance_creation(sender, instance, created, **kwargs):
	if created:
		Shipping.objects.create(order = instance)

@receiver(post_save, sender = Order)
def shipping_instance_save(sender, instance, **kwargs):
	instance.shipping.save()

