from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, ShippingAddress, Comment


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length = 150)
	last_name = forms.CharField(max_length = 150)

	class Meta:

		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['picture', 'nickname', 'description']

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