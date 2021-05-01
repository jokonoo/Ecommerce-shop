# Generated by Django 3.1.1 on 2020-11-26 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SHOP_APP', '0015_auto_20201126_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='apartment',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='city',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='country',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='SHOP_APP.order'),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='phone',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='street',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='zipcode',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]