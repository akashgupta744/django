# Generated by Django 4.2.7 on 2024-01-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('scode', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=100)),
                ('sprinc', models.CharField(max_length=100)),
                ('sloc', models.CharField(max_length=100)),
            ],
        ),
    ]