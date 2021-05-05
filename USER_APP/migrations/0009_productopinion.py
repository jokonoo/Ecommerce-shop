# Generated by Django 3.1.7 on 2021-05-05 01:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SHOP_APP', '0021_product_item_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('USER_APP', '0008_comment_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOpinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], max_length=1)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='SHOP_APP.product')),
            ],
        ),
    ]