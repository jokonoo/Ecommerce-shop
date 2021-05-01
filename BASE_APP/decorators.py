from django.contrib.auth.models import Group
from django.http import HttpResponse 
def permission_checking(list_of_groups=[]):
	def wrapper(func):
		def inner_f(request, *args, **kwargs):
			for i in request.user.groups.all():
				if i.name in list_of_groups:
					return func(request, *args, **kwargs)
			return HttpResponse('Not allowed')
		return inner_f
	return wrapper




