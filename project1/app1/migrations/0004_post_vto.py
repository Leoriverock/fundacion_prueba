# Generated by Django 4.2.3 on 2023-09-14 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vto',
            field=models.DateField(blank=True, null=True),
        ),
    ]
