# Generated by Django 4.2.5 on 2023-09-26 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_alter_propertybook_children_alter_propertybook_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='children',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
        migrations.AlterField(
            model_name='propertybook',
            name='guest',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
    ]
