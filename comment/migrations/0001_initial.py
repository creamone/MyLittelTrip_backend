# Generated by Django 4.0.6 on 2022-07-13 05:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=100, unique=True, verbose_name='게시글 유형')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.BigIntegerField(verbose_name='게시글')),
                ('posttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.posttype', verbose_name='게시글 유형')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.BigIntegerField(verbose_name='게시글')),
                ('comment', models.TextField(verbose_name='댓글 내용')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)], verbose_name='평점')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('posttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.posttype', verbose_name='게시글 유형')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
        ),
    ]