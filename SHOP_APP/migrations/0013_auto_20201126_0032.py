# Generated by Django 3.1.1 on 2020-11-25 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0012_order_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SHOP_APP.order'),
        ),
    ]
