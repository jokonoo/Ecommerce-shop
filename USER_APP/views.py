from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ShippingAddressUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from SHOP_APP.models import Order
from .models import Comment

def register_view(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('website-home')
	else:
		form = UserRegisterForm()
	return render(request, 'USER_APP/register.html', {'form' : form})

@login_required
def user_profile_view(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST ,instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
		s_form = ShippingAddressUpdateForm(request.POST, instance = request.user.shippingaddress)
		if u_form.is_valid() and p_form.is_valid() and s_form.is_valid():
			u_form.save()
			p_form.save()
			s_form.save()
			return redirect('user-profile')
	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.profile)
		s_form = ShippingAddressUpdateForm(instance = request.user.shippingaddress)
	context = {'u_form': u_form , 'p_form' : p_form, 's_form': s_form}

	return render(request, 'USER_APP/profile.html', context)

class OrderView(LoginRequiredMixin, ListView):
	paginate_by = 10
	template_name = 'USER_APP/orders.html'
	def get_queryset(self):
		order = Order.objects.filter(user = self.request.user, complete = False)
		return order

class OrderDetailView(LoginRequiredMixin, DetailView):
	model = Order
	template_name = 'USER_APP/current_order.html'
	context_object_name = 'order'
	
