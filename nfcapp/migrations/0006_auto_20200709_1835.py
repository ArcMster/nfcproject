# Generated by Django 3.0.2 on 2020-07-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfcapp', '0005_auto_20200709_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
