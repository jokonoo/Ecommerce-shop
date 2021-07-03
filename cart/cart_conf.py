from WEBSITE_PROJECT.settings import CART_SESSION_KEY

class Cart:
	"""Code of this cart feature is based on code written in book:
	'Django 3 By Example - Third Edition: Build powerful and reliable Python web applications from scratch'
	I highly reccomend reading it because it gives a lot of knowledge about django features :D
	For example this code let me practice with sessions"""
	
	def __init__(self, request):
		self.session = request.session
		self.cart = self.session[CART_SESSION_KEY]
		if not self.cart
			self.cart = self.session[CART_SESSION_KEY] = {}
	
	def add(self, product, quantity):
		product_id = str(product.id)
		"""Checking if id(converted to string) doesn't exists in self.cart dictionary.
		If it does not, then we are adding new key equal to product_id,
		and its value is new dictionary with quantity key, and price key.
		Also we are converting every decimal value to str"""
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity' : 0, 'price' : str(product.price)}
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
		pass



