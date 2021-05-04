from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name ='website-register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'USER_APP/login.html'), name = 'website-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'USER_APP/logout.html'), name = 'website-logout' ),
    path('profile/', views.user_profile_view, name = 'user-profile'),
    path('password-reset/',
    auth_views.PasswordResetView.as_view(template_name = 'USER_APP/password_reset.html', success_url = 'done/' ),
    name = 'password_reset' ),
    
    path('password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name = 'USER_APP/password_reset_done.html'),
    name = 'password_reset_done'),
    
    path('password-reset/confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name = 'USER_APP/password_reset_confirm.html'),
    name = 'password_reset_confirm'),
    
    path('password-reset/complete',
    auth_views.PasswordResetCompleteView.as_view(template_name = 'USER_APP/password_reset_complete.html'),
    name = 'password_reset_complete'),

    path('profile/orders', views.OrderView.as_view(), name = 'order_user_list'),
    path('profile/orders/<int:pk>', views.CurrentOrderView.as_view(), name = 'current_order')
]