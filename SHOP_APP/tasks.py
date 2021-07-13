from django.core.mail import send_mail
from celery import task

@shared_task
def order_confirmation_mail(order_id):
	order_email = Order.objects.get(id = order_id).email
	subject = f'Order created {order_id}'
	message_body = f'Hello! You created new order with id {order_id}!'
	return send_mail(subject, message, 'placeholder', [order_email])

