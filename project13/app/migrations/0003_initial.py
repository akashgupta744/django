# Generated by Django 4.2.7 on 2023-12-08 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_dept_delete_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='emp',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('mgr', models.IntegerField()),
                ('sal', models.IntegerField()),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
