# Generated by Django 3.0.2 on 2020-06-12 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfcapp', '0003_auto_20200612_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='photo',
            field=models.ImageField(default='abcd', upload_to='media'),
            preserve_default=False,
        ),
    ]