from django.db import models


class AreaType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    short_name = models.TextField(null=True, blank=True)
    is_updated = models.BooleanField(null=True, blank=True)
    is_actual = models.BooleanField(null=True, blank=True)


class Area(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.ForeignKey("AreaType", null=True, blank=True, on_delete=models.SET_NULL)
    name = models.TextField(null=True, blank=True)
    short_name = models.TextField(null=True, blank=True)
    is_updated = models.BooleanField(null=True, blank=True)
    is_actual = models.BooleanField(null=True, blank=True)
    only_name = models.TextField(null=True, blank=True)


class GeonimType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    short_name = models.TextField(null=True, blank=True)
    is_updated = models.BooleanField(null=True, blank=True)
    is_actual = models.BooleanField(null=True, blank=True)


class Geonim(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.ForeignKey("GeonimType", null=True, blank=True, on_delete=models.SET_NULL)
    name = models.TextField(null=True, blank=True)
    short_name = models.TextField(null=True, blank=True)
    is_updated = models.BooleanField(null=True, blank=True)
    is_actual = models.BooleanField(null=True, blank=True)
    only_name = models.TextField(null=True, blank=True)


class Subrf(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    short_name = models.TextField(null=True, blank=True)
    is_updated = models.BooleanField(null=True, blank=True)
    is_actual = models.BooleanField(null=True, blank=True)


class Town(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    short_name = models.TextField(null=True, blank=True)
    search_index = models.TextField(null=True, blank=True)
    is_updated = models.BooleanField(null=True, blank=True)
    is_actual = models.BooleanField(null=True, blank=True)
    has_buildings = models.BooleanField(null=True, blank=True)


class Prefix(models.Model):
    id = models.IntegerField(primary_key=True)
    town = models.ForeignKey("Town", null=True, blank=True, on_delete=models.SET_NULL)
    geonim = models.ForeignKey("Geonim", null=True, blank=True, on_delete=models.SET_NULL)
    area = models.ForeignKey("Area", null=True, blank=True, on_delete=models.SET_NULL)
    toponim_id = models.IntegerField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    short_name = models.TextField(null=True, blank=True)
    search_index = models.TextField(null=True, blank=True)
    is_updated = models.BooleanField(null=True, blank=True)
    is_actual = models.BooleanField(null=True, blank=True)
    sub_rf = models.ForeignKey("Subrf", null=True, blank=True, on_delete=models.SET_NULL)
    has_buildings = models.BooleanField(null=True, blank=True)


class District(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    is_updated = models.BooleanField(null=True, blank=True)
    is_actual = models.BooleanField(null=True, blank=True)


class Building(models.Model):
    id = models.IntegerField(primary_key=True)
    prefix = models.ForeignKey("Prefix", null=True, blank=True, on_delete=models.SET_NULL)
    district = models.ForeignKey("District", null=True, blank=True, on_delete=models.SET_NULL)
    house = models.TextField(null=True, blank=True)
    corpus = models.TextField(null=True, blank=True)
    liter = models.TextField(null=True, blank=True)
    villa = models.TextField(null=True, blank=True)
    parcel = models.TextField(null=True, blank=True)
    full_address = models.TextField(null=True, blank=True)
    is_updated = models.BooleanField(null=True, blank=True)
    is_actual = models.BooleanField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    municipality_id = models.IntegerField(null=True, blank=True)
    short_address = models.TextField(null=True, blank=True)
    post_prefix = models.TextField(null=True, blank=True)
    build_number = models.TextField(null=True, blank=True)
