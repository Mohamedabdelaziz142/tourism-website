# Generated by Django 4.2.5 on 2023-09-22 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_property_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='children',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], max_length=2),
        ),
        migrations.AlterField(
            model_name='propertybook',
            name='guest',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], max_length=2),
        ),
    ]
