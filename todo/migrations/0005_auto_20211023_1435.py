# Generated by Django 3.2.8 on 2021-10-23 17:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20211022_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 10, 23, 17, 35, 7, 191739, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 17, 35, 20, 215664, tzinfo=utc)),
            preserve_default=False,
        ),
    ]