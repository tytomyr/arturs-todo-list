# Generated by Django 4.1.7 on 2023-04-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_optional_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='the_boolean',
            field=models.BooleanField(default=True),
        ),
    ]