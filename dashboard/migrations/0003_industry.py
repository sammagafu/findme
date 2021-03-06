# Generated by Django 3.2.5 on 2021-07-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_category_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(max_length=100, verbose_name='Industry Name')),
                ('icon', models.ImageField(upload_to='Industry/', verbose_name='Avatar')),
                ('description', models.TextField()),
            ],
        ),
    ]
