# Generated by Django 3.1.1 on 2020-09-30 22:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BASE_APP', '0003_auto_20200925_0059'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Postuser',
            new_name='News',
        ),
    ]
