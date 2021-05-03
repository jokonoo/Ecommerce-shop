from django.contrib.auth.models import Group
from django.http import HttpResponse
from USER_APP.models import Comment

def permission_checking(list_of_groups=[]):
	def wrapper(func):
		def inner_f(request, *args, **kwargs):
			for i in request.user.groups.all():
				if i.name in list_of_groups:
					return func(request, *args, **kwargs)
			return HttpResponse('Not allowed')
		return inner_f
	return wrapper

def user_is_author(func):
	def wrapper(request, pk):
		comment = Comment.objects.get(pk = pk)
		if request.user == comment.author:
			return func(request, pk)
		else:
			return HttpResponse('You are not allowed to edit this comment')
	return wrapper	




