# Generated by Django 5.0.6 on 2024-05-13 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tobacco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MixCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
            ],
            options={
                'verbose_name': 'mix category',
                'verbose_name_plural': 'mix categories',
            },
        ),
        migrations.CreateModel(
            name='MixTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
            ],
            options={
                'verbose_name': 'mix tag',
                'verbose_name_plural': 'mix tags',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
            ],
            options={
                'verbose_name': 'variant',
                'verbose_name_plural': 'variants',
            },
        ),
        migrations.CreateModel(
            name='Mix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mix.mixcategory', verbose_name='category')),
                ('tags', models.ManyToManyField(blank=True, to='mix.mixtag', verbose_name='tags')),
                ('variants', models.ManyToManyField(blank=True, to='mix.variant', verbose_name='variants')),
            ],
            options={
                'verbose_name': 'mix',
                'verbose_name_plural': 'mixes',
            },
        ),
        migrations.CreateModel(
            name='Strength',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.PositiveIntegerField(verbose_name='percentage')),
                ('mix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strengths', to='mix.mix', verbose_name='mix')),
                ('tobacco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strengths', to='tobacco.tobacco', verbose_name='tobacco')),
            ],
        ),
    ]
