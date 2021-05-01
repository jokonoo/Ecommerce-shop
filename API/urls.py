from django.urls import path
from . import views
from rest_framework.authtoken import views as rest

urlpatterns = [
	path('products/', views.ProductAPIView.as_view(), name = 'product_api_view'),
    path('products/<pk>/', views.ProductDetailAPIView.as_view(), name = 'product_detail_api_view'),
    path('orders/', views.OrderAPIView.as_view(), name = 'order_api_view'),
    path('orders/<transaction_id>', views.OrderDetailAPIView.as_view(), name = 'order_detail_api_view'),
    path('', views.RootView.as_view(), name= 'root')
]

urlpatterns += [
    path('token/', rest.obtain_auth_token)
]
	

