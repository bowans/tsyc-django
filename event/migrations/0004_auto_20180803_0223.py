# Generated by Django 2.1 on 2018-08-02 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_eventimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventimage',
            name='is_cover',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='eventimage',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='event.Event'),
        ),
    ]
