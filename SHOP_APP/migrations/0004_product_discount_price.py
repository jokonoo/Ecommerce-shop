# Generated by Django 3.1.1 on 2020-10-20 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0003_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]