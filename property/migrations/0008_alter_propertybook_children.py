# Generated by Django 4.2.5 on 2023-10-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_property_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='children',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=0),
        ),
    ]
