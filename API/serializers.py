from rest_framework import serializers
from SHOP_APP.models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(
		view_name = 'product_detail_api_view',
		lookup_field = 'pk')
	class Meta:
		model = Product
		fields = [
		'url',
		'name',
		'price',
		'discount_price',
		'digital',
		'image',
		'slug',
		'description',
		'category',
		'quantity',
		'item_id',
		'pk'
		]

class UserOrderSerializer(serializers.ModelSerializer):
	user = serializers.StringRelatedField()
	products = serializers.StringRelatedField(many = True)
	url = serializers.HyperlinkedIdentityField(
		view_name = 'order_detail_api_view',
		lookup_field = 'transaction_id')
	#products = serializers.HyperlinkedRelatedField(
    #    many=True,
    #    read_only = True,
    #    view_name='product_detail_api_view',
    #    lookup_field = 'pk')
	class Meta:
		model = Order
		fields = [
		'url',
		'user',
		'date_ordered',
		'complete',
		'transaction_id',
		'products',
		'payment_method',
		'total_cost'
		]