# Generated by Django 3.1.1 on 2020-11-05 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('USER_APP', '0003_auto_20201105_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
