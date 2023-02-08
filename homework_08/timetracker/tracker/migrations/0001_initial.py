# Generated by Django 3.2 on 2023-01-17 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epic_name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True, verbose_name='epic_description')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True, verbose_name='task_description')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('hours', models.SmallIntegerField(default=0)),
                ('minutes', models.IntegerField(default=0)),
                ('epic', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='tracker.epic')),
            ],
        ),
    ]
