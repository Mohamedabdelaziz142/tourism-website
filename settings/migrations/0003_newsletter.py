# Generated by Django 4.2.5 on 2023-10-10 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_settings_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateField(default=datetime.datetime(2023, 10, 10, 14, 9, 17, 211102, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
