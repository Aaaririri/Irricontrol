# Generated by Django 3.2.8 on 2021-10-24 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
