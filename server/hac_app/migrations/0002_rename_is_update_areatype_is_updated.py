# Generated by Django 4.2.4 on 2023-08-25 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hac_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='areatype',
            old_name='is_update',
            new_name='is_updated',
        ),
    ]
