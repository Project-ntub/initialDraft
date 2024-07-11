# Generated by Django 5.0.6 on 2024-07-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app113209', '0016_rolepermission_can_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='role',
            name='module',
            field=models.CharField(default='default_module_value', max_length=50),
            preserve_default=False,
        ),
    ]