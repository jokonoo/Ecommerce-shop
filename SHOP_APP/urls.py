from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopView.as_view(), name ='website_shop'),
    path('category/<category>/', views.CategoryView.as_view(), name = 'category_shop'),
    path('product/<slug>', views.ProductDetailView.as_view(), name = 'product_details'),
    path('add-to-cart/<slug>', views.add_to_cart, name = 'add_to_cart'),
    path('remove-from-cart/<slug>', views.remove_from_cart, name = 'remove_from_cart'),
    path('remove-single/<slug>', views.remove_single_item_from_cart, name = 'remove_single'),
    path('cart/', views.cartview, name = 'cart'),
    path('summary/', views.summaryview, name = 'summary_shop'),
    path('checkout/', views.checkoutview, name = 'checkout_shop')
    ]