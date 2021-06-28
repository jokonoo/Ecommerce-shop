from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length = 200, unique = True, db_index = True)
    slug = models.SlugField(max_length = 200, unique = True, db_index = True, blank = True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):

    CATEGORIES = [
    ('C1', 'Category1'),
    ('C2', 'Category2'),
    ('C3', 'Category3'),
    ('C4', 'Category4')]
    
    name = models.CharField(max_length = 200, null = True)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    discount_price = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, null = True)
    available = models.BooleanField(default = True)
    digital = models.BooleanField(default = False, null = True, blank = True)
    image = models.ImageField(upload_to = 'ProductImages' , default = 'default.jpg', null = True, blank = True)
    slug = models.SlugField()
    description = models.TextField(null = True, blank = True)
    category = models.CharField(max_length = 2, choices = CATEGORIES, default = 'C1')
    category1 = models.ForeignKey(Category, db_index = True, related_name = 'products', on_delete = models.CASCADE, blank = True, null = True)
    quantity = models.IntegerField(default = 0)
    api_link = models.TextField(blank = True, null = True)

    def save(self, *args, **kwargs):
        #self.api_link ='http://127.0.0.1:8000'+reverse('api_detail_view', kwargs = {
        #    'slug' : self.slug
        #    })
        super().save()

        img = Image.open(self.image.path)
        output_size = (256, 256)
        
        if img.height > 256 or img.width > 256 or img.width < 256 or img.height <256:
            img = img.resize(output_size, Image.ANTIALIAS)
            img.save(self.image.path)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def get_slug(self):
        return reverse('product_details', kwargs = {
            'slug' : self.slug
    })

    def cartItemURL(self):
        return reverse('add_to_cart', kwargs = {
            'slug' : self.slug
    })

    def cartItemRemove(self):
        return reverse('remove_from_cart', kwargs = {
            'slug' : self.slug
    })

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    product = models.ForeignKey(Product, null = True, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    @property
    def get_total(self):
        if self.product.discount_price:
            return self.product.discount_price * self.quantity
        else:
            return self.product.price * self.quantity
    
    def __str__(self):
        return f'Name: {self.product.name}, Quantity: {self.quantity}'

class Order(models.Model):
    
    PAYMENT_METHODS = [
    ('S', 'Stripe'),
    ('P', 'Paypal')]

    user = models.ForeignKey(User, null = True, blank = True, on_delete = models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default=False, null = True, blank = True)
    transaction_id = models.CharField(max_length = 200, null = True)
    products = models.ManyToManyField(OrderItem)
    payment_method = models.CharField(max_length = 1, choices = PAYMENT_METHODS)
    total_cost = models.IntegerField(default = 0, null = True, blank = True)

    @property
    def get_cart_total(self):
        orderitems = self.products.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.products.all()
        total = sum([item.quantity for item in orderitems])
        return total

    def __str__(self):
        return str(self.transaction_id)

class Shipping(models.Model):

    SHIPPING_METHODS = [
    ('PA', 'Parcel locker'),
    ('PP', 'Personal pickup'),
    ('P', 'Post'),
    ('C', 'Courier')]

    order = models.OneToOneField(Order, null = True, on_delete = models.SET_NULL)
    shipping_method = models.CharField(max_length = 2, choices = SHIPPING_METHODS, null = True, blank = True)
    shipping_cost = models.IntegerField(default = 1)

    def __str__(self):
        return f"{self.order.user.username}'s order"

class BillingAddress(models.Model):
    user = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    order = models.OneToOneField(Order, null = True, on_delete = models.CASCADE)
    country = models.CharField(max_length = 200, null = True, default=None)
    city = models.CharField(max_length = 200, null = True, default=None)
    street = models.CharField(max_length = 200, null = True, default=None)
    apartment = models.CharField(max_length = 200, null = True, default=None)
    zipcode = models.CharField(max_length = 200, null = True, default=None)
    phone = models.CharField(max_length = 200, null = True, default=None)
    date_added = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f'{self.user.username} order of {self.order.pk}'