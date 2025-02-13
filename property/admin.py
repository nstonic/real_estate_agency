from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']
    inlines = [OwnersInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ('flat', 'text')
    list_display = ['user', 'flat', 'text']
    raw_id_fields = ['flat']
    list_filter = ['user']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['full_name']
    list_display = ['full_name', 'pure_phone']
    raw_id_fields = ['flats']
