# Generated by Django 3.2.8 on 2021-10-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_todo_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(editable=False),
        ),
    ]
