# Generated by Django 5.1.7 on 2025-04-11 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schools', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='SchoolName',
        ),
        migrations.CreateModel(
            name='CourseResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live_link', models.URLField(editable=False, max_length=500)),
                ('recorded_link', models.URLField(editable=False, max_length=500)),
                ('courseId', models.ForeignKey(db_column='CourseId', on_delete=django.db.models.deletion.CASCADE, to='Schools.course')),
            ],
        ),
    ]
