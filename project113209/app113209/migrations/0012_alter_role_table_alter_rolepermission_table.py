# Generated by Django 5.0.6 on 2024-07-08 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app113209', '0011_record_current_state'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='role',
            table='role',
        ),
        migrations.AlterModelTable(
            name='rolepermission',
            table='rolepermission',
        ),
    ]
