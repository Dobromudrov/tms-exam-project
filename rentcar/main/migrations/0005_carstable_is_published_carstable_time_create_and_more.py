# Generated by Django 4.0.3 on 2022-04-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_carstable_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='carstable',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='carstable',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='carstable',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
