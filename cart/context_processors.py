from .cart_conf import Cart

def cart(request):
	return {'cart' : Cart(request)}