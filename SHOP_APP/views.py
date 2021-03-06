from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem, BillingAddress, Shipping, Category
from USER_APP.models import ProductOpinion
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from django.views import View
from django.views.decorators.http import require_POST
from django.utils import timezone
from .forms import OrderCreationForm, ShippingUpdateForm, BillingAddressForm, PaymentMethodForm, FilterForm, AddToCartForm
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from cart.cart_conf import Cart

def shop_view(request, category_slug = None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available = True)
	if category_slug:
		category = get_object_or_404(Category, slug = category_slug)
		products = products.filter(categories = category)
	paginator = Paginator(products, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'SHOP_APP/shop.html',
		{'category' : category,
		 'categories' : categories,
		 'page_obj' : page_obj})

#class ShopView(ListView):
#	paginate_by = 10
#	model = Product
#	template_name = 'SHOP_APP/shop.html'
#
#	def get_context_data(self, **kwargs):
#		context = super().get_context_data(**kwargs)
#		context['products'] = Product.objects.filter(available = True)
#		return context

#class CategoryView(ListView):
#	paginate_by = 10
#	model = Product
#	template_name = 'SHOP_APP/categorypage.html'
#
#	def get_queryset(self):
#		context = Product.objects.filter(category = self.kwargs.get('category'))
#		return context

class ProductDetailView(DetailView):
	model = Product
	template_name = 'SHOP_APP/details.html'
	context_object_name = 'product'


	def get_context_data(self, **kwargs):
		product = Product.objects.get(slug = self.kwargs.get('slug'))
		opinions = product.productopinion_set.all().order_by('date')
		
		paginator = Paginator(opinions, 10)
		page_number = self.request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		
		context = super().get_context_data(**kwargs)
		context['opinions'] = opinions
		context['page_obj'] = page_obj
		context['cart_add_form'] = AddToCartForm()
		return context

@require_POST
def add_to_cart(request, product_id, product_slug):
	new_cart = Cart(request)
	product = get_object_or_404(Product, id = product_id, slug = product_slug)
	cart_form = AddToCartForm(request.POST)
	if cart_form.is_valid():
		quantity = cart_form.cleaned_data.get('quantity')
		update = cart_form.cleaned_data.get('update')
		new_cart.add(product, quantity, update)
		messages.info(request, 'Added product to cart')
	return redirect('cart')

def remove_from_cart(request, product_id, product_slug, all = False):
	cart = Cart(request)
	if not all:
		product = get_object_or_404(Product, id = product_id, slug = product_slug)
		cart.remove(product)
		messages.info(request, 'Removed product from cart')
	else: 
		cart.clear()
	return redirect('cart')

def cartview(request):
	cart_object = Cart(request)
	for item in cart_object:
		item['quantity_form'] = AddToCartForm(initial={'quantity' : item['quantity'], 'update' : True})
	return render(request, 'SHOP_APP/cart.html', {'cart_object': cart_object})

def order_creation(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreationForm(request.POST)
		if form.is_valid():
			new_order = form.save()
			for product in cart:
				OrderItem.objects.create(
					order = new_order,
					quantity = product['quantity'],
					product = product['product'],
					price = product['price'])
			cart.clear()
			return render(request, 'SHOP_APP/order_created.html', {'new_order' : new_order})
	else:
		form = OrderCreationForm()
		return render(request, 'SHOP_APP/order_creation.html', {'form' : form})

class ProductFilteringFormView(FormView):
	form_class = FilterForm
	template_name = 'SHOP_APP/filterform.html'
	success_url = reverse_lazy('website_shop')

	def form_valid(self, form):
		context_data = form.cleaned_data
		for k,v in context_data.items():
			if v == None:
				context_data[k] = 0
		return redirect(self.send_data_from_view(context_data))

	def send_data_from_view(self, context_data):
		return reverse('filter_products_display', kwargs = {
			'category' : context_data.get('categories'),
			'lowest' : context_data.get('lowest'),
			'highest' : context_data.get('highest')
			})

def filter_products_view(request, category, lowest, highest):
	if highest == '0':
		highest = '10000'
	lowest, highest = int(lowest), int(highest)
	products = []
	category = (category,)
	
	def filtering(products, item = None, many = False, category = str(category[0])):
		if many == True:
			for i in item:
				if i.discount_price:
					if i.discount_price >= lowest and i.discount_price <= highest:
						products.append(i)
				else:
					if i.price >= lowest and i.price <= highest:
						products.append(i)
			if len(products) < 1:
				category = 'Products not found'
			return products, category
		else:
			if item.discount_price:
				if item.discount_price >= lowest and item.discount_price < highest:
					products.append(item)
				else:
					category = 'Products not found'
			else:
				if item.price >= lowest and item.price <= highest:
					products.append(item)
			return products, category
	
	if len(Product.objects.filter(categories__name__in = category)) > 1:
		products, category = filtering(
			item = Product.objects.filter(categories__name__in = category),
			many = True,
			products = products
			) 
	elif len(Product.objects.filter(categories__name__in = category)) == 1:
		i = Product.objects.get(categories__name__in = category)
		products, category = filtering(
			item = Product.objects.get(categories__name__in = category),
			products = products
			)
	else:	
		return render(request, 'SHOP_APP/filterpage.html', context = {'blank' : True})

	paginator = Paginator(products, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'SHOP_APP/filterpage.html', context = {'products' : products, 'page_obj' : page_obj, 'category' : category})

class OpinionCreateView(LoginRequiredMixin, CreateView):
	model = ProductOpinion
	fields = ['rating', 'content']
	template_name = 'SHOP_APP/opinioncreation.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		form.instance.product = Product.objects.get(pk = self.kwargs.get('product'))
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('product_details', kwargs = {'slug' : Product.objects.get(pk = self.kwargs.get('product')).slug})

#class ShopView(ListView):
#	paginate_by = 10
#	model = Product
#	template_name = 'SHOP_APP/shop.html'
#
#	def get_context_data(self, **kwargs):
#		context = super().get_context_data(**kwargs)
#		context['products'] = Product.objects.filter(available = True)
#		return context

#class CategoryView(ListView):
#	paginate_by = 10
#	model = Product
#	template_name = 'SHOP_APP/categorypage.html'
#
#	def get_queryset(self):
#		context = Product.objects.filter(category = self.kwargs.get('category'))
#		return context

#@login_required
#def add_to_cart(request, slug):
#	product = get_object_or_404(Product, slug = slug)
#	order_item, created = OrderItem.objects.get_or_create(product = product, user = request.user)
#	order_qs = Order.objects.filter(user = request.user, complete = False)
#	if order_qs.exists():
#		order = order_qs[0]
#		if order.products.filter(product__slug = product.slug).exists():
#			order_item.quantity += 1
#			order_item.save()
#			messages.info(request, 'Updated the item quantity')
#			return redirect('cart')
#		else:
#			order.products.add(order_item)
#			messages.info(request, 'Added new item to cart')
#			return redirect('cart')
#	else: 
#		order = Order.objects.create(user = request.user, complete = False)
#		order.products.add(order_item)
#		messages.info(request, 'Added new item to cart')
#		return redirect('product_details', slug = slug)

#@login_required
#def remove_from_cart(request, slug):
#	item = get_object_or_404(Product, slug = slug)
#	order_qs = Order.objects.filter(user = request.user, complete = False)
#	if order_qs.exists():
#		order = order_qs[0]
#		if order.products.filter(product__slug = item.slug).exists():
#			order_item = OrderItem.objects.filter(product = item, user = request.user)[0]
#			order_item.delete()
#			messages.warning(request, 'Items removed from cart.')
#			return redirect('cart')
#		else:
#			messages.warning(request, 'Item does not exist.')
#			return redirect('cart')
#	else :
#		messages.warning(request, 'Order does not exist.')
#		return redirect('cart')

#@login_required
#def remove_single_item_from_cart(request, slug):
#	item = get_object_or_404(Product, slug = slug)
#	order_item, created = OrderItem.objects.get_or_create(product = item, user = request.user)
#	order_qs = Order.objects.filter(user = request.user, complete = False)
#	if order_qs.exists():
#		order = order_qs[0]
#		if order.products.filter(product__slug = item.slug).exists():
#			order_item.quantity -= 1
#			order_item.save()
#			if order_item.quantity <= 0:
#				return redirect('remove_from_cart', slug = slug)
#			else:
#				messages.info(request, 'Updated the item quantity')
#				return redirect('cart')
#		else:
#			messages.warning(request, 'Item is not in cart')
#			return redirect('cart')
#	else :
#		messages.warning(request, 'Order does not exist')
#		return redirect('cart')

#@login_required
#def cartview(request):
#	try:
#		order = Order.objects.get(user = request.user , complete = False)
#		context = {'order' : order}
#		return render(request, 'SHOP_APP/cart.html', context)
#	except Order.DoesNotExist:
#		messages.warning(request, 'Your cart is empty.')
#		return redirect('website_shop')


#@login_required
#def summaryview(request):
#	try:
#		base = Order.objects.get(user = request.user , complete = False)
#		if request.method == 'POST':
#			form = ShippingUpdateForm(request.POST, instance = base.shipping)
#			if form.is_valid():
#				form.save()
#				return redirect('checkout_shop')
#		else:
#			form = ShippingUpdateForm(instance = base.shipping)
#			context = {'order' : base.products.all(), 'base' : base, 'form' : form}
#		return render(request, 'SHOP_APP/summary.html', context)
#	except Order.DoesNotExist:
#		raise Http404('Order does not exist')
#		return redirect('website_shop')
#
#@login_required
#def checkoutview(request):
#	order = Order.objects.get(user = request.user, complete = False)
#	address, created = BillingAddress.objects.get_or_create(user = request.user, order = order)
#	if created:
#		address = BillingAddress.objects.get(user = request.user, order = order)
#		if request.method == 'POST':
#			form_1 = BillingAddressForm(request.POST, instance = address)
#			form_2 = PaymentMethodForm(request.POST, instance = order)
#			if form_1.is_valid() and form_2.is_valid():
#				form_1.save()
#				form_2.save()
#				return redirect('website_shop')
#		else:
#			form_1 = BillingAddressForm(instance = address)	
#			form_2 = PaymentMethodForm(instance = order)
#			context = {'form_1' : form_1, 'form_2' : form_2, 'address' : address, 'order' : order}
#		return render(request, 'SHOP_APP/checkout.html', context)
#	else:
#		if request.method == 'POST':
#			form_1 = BillingAddressForm(request.POST, instance = address)
#			form_2 = PaymentMethodForm(request.POST, instance = order)
#			if form_1.is_valid() and form_2.is_valid():
#				form_1.save()
#				form_2.save()
#				return redirect('website_shop')
#		else:
#			form_1 = BillingAddressForm(instance = address)	
#			form_2 = PaymentMethodForm(instance = order)
#			context = {'form_1' : form_1, 'form_2' : form_2, 'address' : address, 'order' : order}
#		return render(request, 'SHOP_APP/checkout.html', context)
