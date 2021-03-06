# Generated by Django 2.1.7 on 2019-03-17 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_event_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('link', models.URLField()),
                ('event', models.ForeignKey(help_text='which event the talk as given at', on_delete=django.db.models.deletion.CASCADE, related_name='talks', to='events.Event')),
                ('speaker', models.ForeignKey(help_text='which speaker gave this talk', on_delete=django.db.models.deletion.CASCADE, related_name='talks', to='events.Speaker')),
            ],
        ),
    ]
