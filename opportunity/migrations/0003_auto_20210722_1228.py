# Generated by Django 3.2.5 on 2021-07-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_industry'),
        ('opportunity', '0002_opportunity_budjet'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='is_negotiatable',
            field=models.BooleanField(default=False, verbose_name='Open for Negotiations'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='dashboard.Category'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='industry',
            field=models.ManyToManyField(blank=True, null=True, to='dashboard.Industry'),
        ),
    ]