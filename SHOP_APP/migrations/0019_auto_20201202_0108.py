# Generated by Django 3.1.1 on 2020-12-02 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0018_auto_20201129_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='ProductImages'),
        ),
    ]
