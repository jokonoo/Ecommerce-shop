from django.shortcuts import render
from SHOP_APP.models import Product, Order
from .serializers import ProductSerializer, UserOrderSerializer
from rest_framework import generics, mixins, permissions, filters, renderers, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from .paginations import OffsetPagination


class ProductAPIView(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
	authentication_classes = [authentication.TokenAuthentication]
	serializer_class = ProductSerializer
	filter_backends = [filters.SearchFilter]
	pagination_class = OffsetPagination
	search_fields = ['name', 'slug', '=item_id']
	queryset = Product.objects.all()

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
	authentication_classes = [authentication.TokenAuthentication]
	serializer_class = ProductSerializer
	queryset = Product.objects
	lookup_field = 'pk'

class OrderAPIView(generics.ListCreateAPIView):
	permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
	authentication_classes = [authentication.TokenAuthentication]
	serializer_class = UserOrderSerializer
	filter_backends = [filters.SearchFilter]
	pagination_class = OffsetPagination
	search_fields = ['user__username', 'date_ordered', 'complete', 'transaction_id']
	queryset = Order.objects.all()

class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
	authentication_classes = [authentication.TokenAuthentication]
	serializer_class = UserOrderSerializer
	queryset = Order.objects.all()
	lookup_field = 'transaction_id'

class RootView(APIView):

	def get(self, request, *args, **kwargs):
		return Response({
			'products' : reverse('product_api_view', request = self.request),
			'orders' : reverse('order_api_view', request = self.request)
			})
