# Generated by Django 2.1.5 on 2019-01-25 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tedxuwa_user', '0006_auto_20180529_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['first_name', 'last_name']},
        ),
    ]
