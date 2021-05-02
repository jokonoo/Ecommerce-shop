from django.urls import path
from . import views

urlpatterns = [
    path('', views.homee, name ='website-home'),
    path('news/', views.NewsListView.as_view(), name ='website-news'),
    path('news/createnews/', views.CreateNewsView.as_view(), name ='website-createnews'),
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name = 'website-updatenews'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name = 'website-deletenews'),
    path('news/<int:pk>', views.news_detail_view, name = 'website-detailnews'),
    path('comment/<int:pk>/edit', views.comment_edit_view, name = 'comment-update'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name = 'comment-delete'),
    path('contact/', views.contact, name ='website-contact')
]