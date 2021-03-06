# Generated by Django 3.2.5 on 2021-07-22 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_industry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('slug', models.SlugField(editable=False, verbose_name='slug')),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is_active')),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='advister')),
                ('category', models.ManyToManyField(to='dashboard.Category')),
                ('industry', models.ManyToManyField(to='dashboard.Industry')),
            ],
            options={
                'verbose_name': 'Opportunity',
                'verbose_name_plural': 'Opportunities',
            },
        ),
    ]
