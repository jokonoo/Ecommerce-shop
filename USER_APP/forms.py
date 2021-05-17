from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, ShippingAddress, Comment
from allauth.account.forms import SignupForm


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length = 150)
	last_name = forms.CharField(max_length = 150)

	class Meta:

		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomSignupForm(SignupForm):
	first_name = forms.CharField(max_length = 150)
	last_name = forms.CharField(max_length = 150)
	
	def signup(self, request, user):
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.save()
		return user

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['picture', 'description']

class ShippingAddressUpdateForm(forms.ModelForm):

	class Meta:
		model = ShippingAddress
		exclude = ['user']

class CreateCommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		exclude = ['author', 'date', 'news']

class UpdateCommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ['content']