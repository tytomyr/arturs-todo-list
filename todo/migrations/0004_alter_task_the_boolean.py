# Generated by Django 4.1.7 on 2023-04-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_task_the_boolean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='the_boolean',
            field=models.BooleanField(default=False),
        ),
    ]
