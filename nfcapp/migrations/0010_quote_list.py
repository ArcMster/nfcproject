# Generated by Django 3.0.2 on 2020-08-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfcapp', '0009_auto_20200809_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=30)),
                ('quote', models.CharField(max_length=255)),
            ],
        ),
    ]
