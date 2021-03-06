# Generated by Django 2.0.6 on 2018-11-01 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20181101_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author_favorites',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='blogdata',
            name='posted_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 1, 19, 4, 24, 690600)),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 1, 19, 4, 24, 690600)),
        ),
    ]
