# Generated by Django 3.2.5 on 2021-07-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='budjet',
            field=models.FloatField(default=100000),
        ),
    ]
