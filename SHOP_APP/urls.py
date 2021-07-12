from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_view, name ='website_shop'),
    path('product/<slug>', views.ProductDetailView.as_view(), name = 'product_details'),
    path('opinion/<product>/create', views.OpinionCreateView.as_view(), name = 'create_opinion'),
    path('add-to-cart/<int:product_id>/<slug:product_slug>', views.add_to_cart, name = 'add_to_cart'),
    path('remove-from-cart/<int:product_id>/<slug:product_slug>', views.remove_from_cart, name = 'remove_from_cart'),
    path('cart/', views.cartview, name = 'cart'),
    path('filter/', views.ProductFilteringFormView.as_view(), name = 'filter_products'),
    path('<category_slug>/', views.shop_view, name= 'filtered_shop'),
    path('filter/<category>/<lowest>/<highest>/', views.filter_products_view, name = 'filter_products_display'),
    path('order/create', views.order_creation, name = 'order_create'),
    #path('category/<category>/', views.CategoryView.as_view(), name = 'category_shop'),
    #path('remove-single/<slug>', views.remove_single_item_from_cart, name = 'remove_single'),
    #path('summary/', views.summaryview, name = 'summary_shop'),
    #path('checkout/', views.checkoutview, name = 'checkout_shop'),
    ]
