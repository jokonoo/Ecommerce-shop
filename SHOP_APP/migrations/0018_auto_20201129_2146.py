# Generated by Django 3.1.1 on 2020-11-29 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0017_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='shipping_cost',
            field=models.IntegerField(default=1),
        ),
    ]
