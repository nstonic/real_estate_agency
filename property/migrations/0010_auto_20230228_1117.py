# Generated by Django 3.2.4 on 2023-02-28 07:17

from django.db import migrations


def create_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            pure_phone=flat.owner_pure_phone,
            defaults={
                'full_name': flat.owner,
                'phonenumber': flat.owners_phonenumber,
            }
        )


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(create_owners)
    ]