# Generated by Django 3.0.4 on 2020-03-27 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covidfitness', '0011_auto_20200327_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchallenge',
            name='repeat',
        ),
    ]
