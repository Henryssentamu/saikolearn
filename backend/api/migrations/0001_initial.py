# Generated by Django 5.1.7 on 2025-03-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=150)),
                ('sname', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=15)),
            ],
        ),
    ]
