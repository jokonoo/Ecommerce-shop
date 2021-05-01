# Generated by Django 3.1.1 on 2020-11-12 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0008_delete_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('C1', 'Category1'), ('C2', 'Category2'), ('C3', 'Category3'), ('C4', 'Category4')], default='C1', max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImages'),
        ),
    ]