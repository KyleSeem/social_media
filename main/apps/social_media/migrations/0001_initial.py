# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-15 15:07
from __future__ import unicode_literals

import apps.social_media.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bricks',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brick', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_media.Brick')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_reg.User')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=apps.social_media.models.upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_reg.User')),
            ],
            options={
                'db_table': 'photos',
            },
        ),
        migrations.AddField(
            model_name='brick',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_media.Photo'),
        ),
        migrations.AddField(
            model_name='brick',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_reg.User'),
        ),
    ]
