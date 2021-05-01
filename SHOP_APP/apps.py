from django.apps import AppConfig


class ShopAppConfig(AppConfig):
    name = 'SHOP_APP'

    def ready(self):
    	import USER_APP.signals

