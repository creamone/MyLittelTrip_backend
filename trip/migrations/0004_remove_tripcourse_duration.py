# Generated by Django 4.0.6 on 2022-07-13 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_tripcourse_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripcourse',
            name='duration',
        ),
    ]