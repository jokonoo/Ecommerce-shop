from django import forms
from .models import Order, Shipping, BillingAddress

class CheckoutForm(forms.Form):
	street = forms.CharField(label = 'Enter your address:', max_length = 200)
	apartment = forms.CharField(label = 'Enter number of your apartment:', max_length = 200)
	city = forms.CharField(label = 'Enter your city:', max_length = 200)
	country = forms.CharField(label = 'Enter your country:', max_length = 200)
	zipcode = forms.CharField(label = 'Enter your zipcode:', max_length = 200)
	phone = forms.CharField(label = 'Enter your phone number:', max_length = 200)

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