from django import forms
from .models import Order, Shipping, BillingAddress, Product, Category

class AddToCartForm(forms.Form):
	CHOICES = [(i, str(i)) for i in range(1,21)] 
	quantity = forms.TypedChoiceField(
		label = 'Select quantity',
		choices = CHOICES,
		coerce = int)
	update = forms.BooleanField(
		required = False,
		initial = False,
		widget = forms.HiddenInput)
	"""Using TypedChoiceField to make sure that quantity key is returning int values"""

class OrderCreationForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

class ShippingUpdateForm(forms.ModelForm):
	shipping_method = forms.ChoiceField(label = 'Select', choices = Shipping.SHIPPING_METHODS)

	class Meta:
		model = Shipping
		fields = ['shipping_method']

class BillingAddressForm(forms.ModelForm):
	
	class Meta:
		model = BillingAddress 
		exclude = ['user', 'order', 'date_added']

class PaymentMethodForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['payment_method']

class FilterForm(forms.Form):
	categories = forms.ChoiceField(label = "Select category", choices =
		[(str(x),str(x)) for x in Category.objects.values_list(
			'name', flat = True)],
			required = False)
	#categories = forms.ChoiceField(label = "Select category", choices = Product.CATEGORIES, required = False)
	lowest = forms.IntegerField(label = "Enter min price", required = False) 
	highest = forms.IntegerField(label = "Enter max price", required = False) 