# Generated by Django 3.0.2 on 2020-08-09 20:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfcapp', '0011_emails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='story',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
