# Generated by Django 4.2.4 on 2023-08-25 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hac_app', '0008_town'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('toponim_id', models.IntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('short_name', models.TextField(blank=True, null=True)),
                ('search_index', models.TextField(blank=True, null=True)),
                ('is_updated', models.BooleanField(blank=True, null=True)),
                ('is_actual', models.BooleanField(blank=True, null=True)),
                ('has_buildings', models.BooleanField(blank=True, null=True)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hac_app.area')),
                ('geonim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hac_app.geonim')),
                ('sub_rf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hac_app.subrf')),
                ('town', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hac_app.town')),
            ],
        ),
    ]
