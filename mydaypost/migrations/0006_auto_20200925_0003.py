# Generated by Django 3.1 on 2020-09-24 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydaypost', '0005_assignmentmodel_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentmodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='assignmentmodel',
            name='updated_at',
        ),
    ]
