# Generated by Django 5.0.6 on 2024-05-13 11:31

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='only_medias/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'avi', 'mov', 'gif', 'webp', 'pdf', 'doc', 'docx', 'mpeg'])], verbose_name='File')),
                ('file_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video'), ('document', 'document'), ('gif', 'Gif'), ('other', 'Other')], max_length=10, verbose_name='File Type')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='CommonSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('stars', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)], verbose_name='Рейтинг')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Common Settings',
                'verbose_name_plural': 'Common Settings',
            },
        ),
    ]
