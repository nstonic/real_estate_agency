# Generated by Django 3.2.4 on 2023-02-28 08:03

from django.db import migrations


def link_owner_to_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all().iterator():
        owner, created = Owner.objects.get_or_create(
            full_name=flat.owner,
            pure_phone=flat.owner_pure_phone,
            defaults={'phonenumber': flat.owners_phonenumber})
        owner.flats.add(flat)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0010_auto_20230228_1117'),
    ]

    operations = [
        migrations.RunPython(link_owner_to_flat)
    ]
