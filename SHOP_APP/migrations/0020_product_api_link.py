# Generated by Django 3.1.1 on 2020-12-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0019_auto_20201202_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='api_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
