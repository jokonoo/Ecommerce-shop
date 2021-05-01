from django.apps import AppConfig


class UserAppConfig(AppConfig):
    name = 'USER_APP'

    def ready(self):
    	import USER_APP.signals
