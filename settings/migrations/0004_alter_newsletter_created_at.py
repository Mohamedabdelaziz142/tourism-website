# Generated by Django 4.2.5 on 2023-10-13 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 10, 13, 11, 14, 20, 465236, tzinfo=datetime.timezone.utc)),
        ),
    ]
