# Generated by Django 5.0.6 on 2024-07-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app113209', '0013_alter_rolepermission_permission_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolepermission',
            name='permission_name',
            field=models.CharField(max_length=100),
        ),
    ]
