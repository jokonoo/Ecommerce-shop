# Generated by Django 3.1.7 on 2021-07-10 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0026_auto_20210711_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
