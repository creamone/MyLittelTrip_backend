# Generated by Django 4.0.6 on 2022-08-03 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0006_alter_tripcourse_tripcoursetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripcourse',
            name='doing',
            field=models.CharField(max_length=100, null=True, verbose_name='여행 코스 내용'),
        ),
    ]