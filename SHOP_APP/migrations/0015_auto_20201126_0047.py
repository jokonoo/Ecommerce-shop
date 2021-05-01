# Generated by Django 3.1.1 on 2020-11-25 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0014_auto_20201126_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='shipping_method',
            field=models.CharField(blank=True, choices=[('PA', 'Parcel locker'), ('PP', 'Personal pickup'), ('P', 'Post'), ('C', 'Courier')], max_length=2, null=True),
        ),
    ]