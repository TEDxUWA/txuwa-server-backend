# Generated by Django 2.0.4 on 2018-05-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180415_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(blank=True, help_text='Australia/Perth time', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(blank=True, help_text='Australia/Perth time', null=True),
        ),
    ]
