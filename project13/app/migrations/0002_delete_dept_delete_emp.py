# Generated by Django 4.2.7 on 2023-12-08 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='dept',
        ),
        migrations.DeleteModel(
            name='emp',
        ),
    ]
