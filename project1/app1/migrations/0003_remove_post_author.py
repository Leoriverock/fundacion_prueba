# Generated by Django 4.2.3 on 2023-09-14 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
