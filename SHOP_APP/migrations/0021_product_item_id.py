# Generated by Django 3.1.1 on 2020-12-25 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0020_product_api_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='item_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]