# Generated by Django 2.0.4 on 2018-05-03 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tedxuwa_user', '0003_auto_20180417_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='is_current',
            new_name='is_comittee',
        ),
    ]
