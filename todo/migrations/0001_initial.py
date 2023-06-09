# Generated by Django 4.1.7 on 2023-04-03 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('optional_deadline', models.DateTimeField(blank=True)),
                ('the_boolean', models.BooleanField()),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.tag')),
            ],
        ),
    ]
