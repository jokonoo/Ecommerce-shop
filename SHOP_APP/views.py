from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem, BillingAddress, Shipping
from USER_APP.models import ProductOpinion
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views import View
from django.utils import timezone
from .forms import CheckoutForm, ShippingUpdateForm, BillingAddressForm, PaymentMethodForm
from django.core.paginator import Paginator

class ShopView(ListView):
	paginate_by = 10
	model = Product
	template_name = 'SHOP_APP/shop.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Product.CATEGORIES
		return context

class CategoryView(ListView):
	paginate_by = 10
	model = Product
	template_name = 'SHOP_APP/categorypage.html'

	def get_queryset(self):
		context = Product.objects.filter(category = self.kwargs.get('category'))
		return context

class ProductDetailView(DetailView):
	model = Product
	template_name = 'SHOP_APP/details.html'
	context_object_name = 'product'

	def get_context_data(self, **kwargs):
		opinions = ProductOpinion.objects.all().order_by('date')
		
		paginator = Paginator(opinions, 10)
		page_number = self.request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		
		context = super().get_context_data(**kwargs)
		context['opinions'] = opinions
		context['page_obj'] = page_obj
		return context

@login_required
def add_to_cart(request, slug):
	product = get_object_or_404(Product, slug = slug)
	order_item, created = OrderItem.objects.get_or_create(product = product, user = request.user)
	order_qs = Order.objects.filter(user = request.user, complete = False)
	if order_qs.exists():
		order = order_qs[0]
		if order.products.filter(product__slug = product.slug).exists():
			order_item.quantity += 1
			order_item.save()
			messages.info(request, 'Updated the item quantity')
			return redirect('cart')
		else:
			order.products.add(order_item)
			messages.info(request, 'Added new item to cart')
			return redirect('cart')
	else: 
		order = Order.objects.create(user = request.user, complete = False)
		order.products.add(order_item)
		messages.info(request, 'Added new item to cart')
		return redirect('product_details', slug = slug)

@login_required
def remove_from_cart(request, slug):
	item = get_object_or_404(Product, slug = slug)
	order_qs = Order.objects.filter(user = request.user, complete = False)
	if order_qs.exists():
		order = order_qs[0]
		if order.products.filter(product__slug = item.slug).exists():
			order_item = OrderItem.objects.filter(product = item, user = request.user)[0]
			order_item.delete()
			messages.warning(request, 'Items removed from cart.')
			return redirect('cart')
		else:
			messages.warning(request, 'Item does not exist.')
			return redirect('cart')
	else :
		messages.warning(request, 'Order does not exist.')
		return redirect('cart')

@login_required
def remove_single_item_from_cart(request, slug):
	item = get_object_or_404(Product, slug = slug)
	order_item, created = OrderItem.objects.get_or_create(product = item, user = request.user)
	order_qs = Order.objects.filter(user = request.user, complete = False)
	if order_qs.exists():
		order = order_qs[0]
		if order.products.filter(product__slug = item.slug).exists():
			order_item.quantity -= 1
			order_item.save()
			if order_item.quantity <= 0:
				return redirect('remove_from_cart', slug = slug)
			else:
				messages.info(request, 'Updated the item quantity')
				return redirect('cart')
		else:
			messages.warning(request, 'Item is not in cart')
			return redirect('cart')
	else :
		messages.warning(request, 'Order does not exist')
		return redirect('cart')

@login_required
def cartview(request):
	try:
		order = Order.objects.get(user = request.user , complete = False)
		context = {'order' : order}
		return render(request, 'SHOP_APP/cart.html', context)
	except Order.DoesNotExist:
		messages.warning(request, 'Your cart is empty.')
		return redirect('website_shop')


@login_required
def summaryview(request):
	try:
		base = Order.objects.get(user = request.user , complete = False)
		if request.method == 'POST':
			form = ShippingUpdateForm(request.POST, instance = base.shipping)
			if form.is_valid():
				form.save()
				return redirect('checkout_shop')
		else:
			form = ShippingUpdateForm(instance = base.shipping)
			context = {'order' : base.products.all(), 'base' : base, 'form' : form}
		return render(request, 'SHOP_APP/summary.html', context)
	except Order.DoesNotExist:
		raise Http404('Order does not exist')
		return redirect('website_shop')

@login_required
def checkoutview(request):
	order = Order.objects.get(user = request.user, complete = False)
	address, created = BillingAddress.objects.get_or_create(user = request.user, order = order)
	if created:
		address = BillingAddress.objects.get(user = request.user, order = order)
		if request.method == 'POST':
			form_1 = BillingAddressForm(request.POST, instance = address)
			form_2 = PaymentMethodForm(request.POST, instance = order)
			if form_1.is_valid() and form_2.is_valid():
				form_1.save()
				form_2.save()
				return redirect('website_shop')
		else:
			form_1 = BillingAddressForm(instance = address)	
			form_2 = PaymentMethodForm(instance = order)
			context = {'form_1' : form_1, 'form_2' : form_2, 'address' : address, 'order' : order}
		return render(request, 'SHOP_APP/checkout.html', context)
	else:
		if request.method == 'POST':
			form_1 = BillingAddressForm(request.POST, instance = address)
			form_2 = PaymentMethodForm(request.POST, instance = order)
			if form_1.is_valid() and form_2.is_valid():
				form_1.save()
				form_2.save()
				return redirect('website_shop')
		else:
			form_1 = BillingAddressForm(instance = address)	
			form_2 = PaymentMethodForm(instance = order)
			context = {'form_1' : form_1, 'form_2' : form_2, 'address' : address, 'order' : order}
		return render(request, 'SHOP_APP/checkout.html', context)