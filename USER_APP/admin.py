from django.contrib import admin
from .models import Profile, ShippingAddress, Comment, ProductOpinion
# Register your models here.

admin.site.register(Profile)
admin.site.register(ShippingAddress)
admin.site.register(Comment)
admin.site.register(ProductOpinion)