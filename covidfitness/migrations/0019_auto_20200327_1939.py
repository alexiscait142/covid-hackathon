# Generated by Django 3.0.4 on 2020-03-27 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidfitness', '0018_auto_20200327_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(default=0, null=True),
        ),
    ]