# Generated by Django 3.1.7 on 2021-07-12 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0029_orderitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]
