# Generated by Django 3.2 on 2023-02-09 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20230209_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='epic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.epic'),
        ),
    ]
