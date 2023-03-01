# Generated by Django 4.1.5 on 2023-01-13 14:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_song_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(20.0)]),
        ),
    ]