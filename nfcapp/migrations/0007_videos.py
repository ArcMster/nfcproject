# Generated by Django 3.0.2 on 2020-07-14 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfcapp', '0006_auto_20200709_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('video_link', models.CharField(max_length=150)),
            ],
        ),
    ]