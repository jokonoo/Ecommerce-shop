from WEBSITE_PROJECT.settings import CART_SESSION_KEY
from SHOP_APP.models import Product
from decimal import Decimal

class Cart:
	"""Code of this cart feature is based on code written in book:
	'Django 3 By Example - Third Edition: Build powerful and reliable Python web applications from scratch'
	I highly reccomend reading it because it gives a lot of knowledge about django features :D
	For example this code let me practice with sessions"""
	
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(CART_SESSION_KEY)
		if not cart:
			cart = self.session[CART_SESSION_KEY] = {}
		self.cart = cart
	
	def add(self, product, quantity, update):
		product_id = str(product.id)
		"""Checking if id(converted to string) doesn't exists in self.cart dictionary.
		If it does not, then we are adding new key equal to product_id,
		and its value is new dictionary with quantity key, and price key.
		Also we are converting every decimal value to str"""
		if product_id not in self.cart:
			if product.discount_price:
				price = product.discount_price
			else:
				price = product.price
			self.cart[product_id] = {'quantity' : 0, 'price' : str(price)}
		
		if update:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		
		self.save()

	def save(self):
		"""Setting self.session.modified to True, because sessions save themselfes only if it was modified.
		Source: https://docs.djangoproject.com/en/3.2/topics/http/sessions/#when-sessions-are-saved"""
		self.session.modified = True
	
	def remove(self, product):
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()
	
	def __iter__(self):
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		"""What we did here was getting all ids of products inside cart,
		 and filtering products to get query with all these products"""
		cart = self.cart.copy()
		for product in products:
			cart[str(product.id)]['product'] = product
		for item in cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item
		"""Creating copy of cart with all its keys and values,
		 and appending product objects to dictionary,
		 and creating new keys with price of product, and its total price,
		 then yielding item so we can access all these values one by one while iterating"""
	
	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

	def clear(self):
		del self.session[CART_SESSION_KEY]
		self.save()
		



