# Generated by Django 3.2.5 on 2021-07-29 14:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opportunity', '0007_auto_20210728_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliedjob',
            name='saved',
        ),
        migrations.AlterField(
            model_name='appliedjob',
            name='applied',
            field=models.BooleanField(default=True, verbose_name='Applied'),
        ),
        migrations.AlterField(
            model_name='appliedjob',
            name='applied_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 29, 14, 26, 17, 323257, tzinfo=utc), verbose_name='Start Date'),
        ),
        migrations.CreateModel(
            name='SavedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_saved', models.BooleanField(default=True, verbose_name='Applied')),
                ('saved_date', models.DateField(default=datetime.datetime(2021, 7, 29, 14, 26, 17, 323626, tzinfo=utc), verbose_name='Start Date')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opportunity.opportunity', verbose_name='Opportunity')),
                ('saving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Person Applying')),
            ],
        ),
    ]