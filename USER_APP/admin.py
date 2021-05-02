from django.contrib import admin
from .models import Profile, ShippingAddress, Comment
# Register your models here.

admin.site.register(Profile)
admin.site.register(ShippingAddress)
admin.site.register(Comment)