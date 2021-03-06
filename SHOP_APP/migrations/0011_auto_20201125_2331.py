# Generated by Django 3.1.1 on 2020-11-25 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0010_auto_20201122_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_method',
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_method', models.CharField(choices=[('PA', 'Parcel locker'), ('PP', 'Personal pickup'), ('P', 'Post'), ('C', 'Courier')], max_length=2)),
                ('shipping_cost', models.IntegerField(blank=True, default=1, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SHOP_APP.order')),
            ],
        ),
    ]
