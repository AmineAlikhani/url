# Generated by Django 4.0.4 on 2022-06-28 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UrlData',
            new_name='Url',
        ),
    ]