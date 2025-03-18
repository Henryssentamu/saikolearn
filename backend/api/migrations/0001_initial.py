# Generated by Django 5.1.7 on 2025-03-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterStudent',
            fields=[
                ('date', models.DateField(auto_now_add=True)),
                ('studentid', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fName', models.CharField(max_length=150)),
                ('sname', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('phonenumber', models.CharField(max_length=15, unique=True)),
                ('country', models.CharField(max_length=100)),
                ('dateofbirth', models.DateField()),
                ('gender', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
    ]
