# Generated by Django 3.1 on 2020-09-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydaypost', '0003_auto_20200924_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
