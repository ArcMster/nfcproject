# Generated by Django 3.0.2 on 2020-07-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfcapp', '0004_stories_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='photo',
            field=models.ImageField(default='media/default.png', upload_to='media'),
        ),
    ]
