# Generated by Django 3.1.1 on 2020-10-19 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0002_orderitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='SHOP_APP.Product'),
        ),
    ]