# Generated by Django 5.0.6 on 2024-07-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app113209', '0012_alter_role_table_alter_rolepermission_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolepermission',
            name='permission_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
