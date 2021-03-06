from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .decorators import permission_checking, user_is_author
from .models import News

from USER_APP.forms import CreateCommentForm , UpdateCommentForm
from USER_APP.models import Comment

from datetime import datetime

#@permission_checking(['admin'])
def homee(request):
	now = datetime.now().strftime("%d/%m/%Y %H:%M")
	return render(request, 'BASE_APP/index.html', {"now" : now})

def contact(request):
	return render(request, 'BASE_APP/contact.html')

class NewsListView(ListView):
	paginate_by = 10
	queryset = News.objects.all().order_by('-date_posted')
	template_name = 'BASE_APP/newspage.html'

def news_detail_view(request, pk):
	news = News.objects.get(pk = pk)
	comments = Comment.objects.filter(news = news).order_by('date')
	paginator = Paginator(comments, 10)
	if request.method == 'POST':
		form = CreateCommentForm(request.POST)
		if form.is_valid():
			new = form.save(commit = False)
			new.author = request.user
			new.news = news
			new.save()
			return redirect('website-detailnews', pk = pk)
	else:
		form = CreateCommentForm()
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
	return render(request, 'BASE_APP/detailnews.html', context = {'object' : news, 'comments' : comments, 'form' : form, 'page_obj': page_obj})

@login_required
@user_is_author
def comment_edit_view(request, pk):
	comment = Comment.objects.get(pk = pk)
	if request.user == comment.author:
		if request.method == 'POST':
			form = UpdateCommentForm(request.POST, instance = comment)
			if form.is_valid():
				form.save()
				return redirect('website-detailnews', comment.news.pk)
		else:
			form = UpdateCommentForm(instance = comment)
	else:
		return redirect('website-detailnews', comment.news.pk)
	return render(request, 'BASE_APP/commentedit.html', context = {'form' : form})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Comment
	template_name = 'BASE_APP/deletecomment.html'

	def test_func(self):
		if self.get_object().author == self.request.user:
			return True
		else:
			return False

	def get_success_url(self, *args, **kwargs):
		object = Comment.objects.get(pk = self.kwargs.get('pk'))
		return reverse_lazy('website-detailnews', args=(object.news.pk,))

class CreateNewsView(LoginRequiredMixin, PermissionRequiredMixin ,CreateView):
	permission_required = 'BASE_APP.can_create_news'
	model = News
	template_name = 'BASE_APP/createnews.html'
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class UpdateNewsView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
	permission_required = ('BASE_APP.can_create_news', 'BASE_APP_can_update_news')
	model = News
	template_name = 'BASE_APP/updatenews.html'
	fields = ['title', 'content']

	def test_func(self):
		if self.get_object().author == self.request.user:
			return True
		else:
			return False

class DeleteNewsView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
	permission_required = ('BASE_APP.can_create_news', 'BASE_APP_can_update_news')
	model = News
	template_name = 'BASE_APP/deletenews.html'
	success_url = reverse_lazy('website-news')