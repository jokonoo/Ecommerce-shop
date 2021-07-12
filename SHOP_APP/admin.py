from django.contrib import admin
from .models import Product, Order, OrderItem, BillingAddress, Shipping, Category
# Register your models here.

admin.site.register(Product)
admin.site.register(BillingAddress)
admin.site.register(Shipping)
admin.site.register(Category)

class OrderItemInline(admin.TabularInline):
	model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_filter = ['completed', 'date_ordered', 'date_completed']
	inlines = [OrderItemInline]


