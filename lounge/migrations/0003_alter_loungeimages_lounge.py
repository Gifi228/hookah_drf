# Generated by Django 5.0.6 on 2024-05-13 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lounge', '0002_alter_lounge_rate_google_alter_lounge_rate_yandex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loungeimages',
            name='lounge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lounge_images', to='lounge.lounge', verbose_name='lounge'),
        ),
    ]