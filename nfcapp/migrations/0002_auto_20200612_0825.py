# Generated by Django 3.0.2 on 2020-06-12 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfcapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='name',
            field=models.TextField(max_length=30),
        ),
    ]