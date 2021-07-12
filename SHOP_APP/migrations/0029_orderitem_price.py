# Generated by Django 3.1.7 on 2021-07-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0028_remove_order_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]