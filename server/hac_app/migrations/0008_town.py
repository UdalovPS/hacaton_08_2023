# Generated by Django 4.2.4 on 2023-08-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hac_app', '0007_subrf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('short_name', models.TextField(blank=True, null=True)),
                ('search_index', models.TextField(blank=True, null=True)),
                ('is_updated', models.BooleanField(blank=True, null=True)),
                ('is_actual', models.BooleanField(blank=True, null=True)),
                ('has_buildings', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
