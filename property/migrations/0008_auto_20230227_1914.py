# Generated by Django 2.2.4 on 2023-02-27 15:14
from django.db import migrations
import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.filter(owners_phonenumber__isnull=False):
        parsed_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_phone):
            flat.owner_pure_phone = parsed_phone
            flat.save(update_fields=['owner_pure_phone'])


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0007_auto_20230227_1912'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers)
    ]
