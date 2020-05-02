from django.contrib import admin
from .models import *
# from solarpvsite.models import User

# Register your models here.
# admin.site.register(Client)
admin.site.register(Location)
# admin.site.register(Product)
admin.site.register(User)
# admin.site.register(Certificate)
admin.site.register(Service)
admin.site.register(Performance)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['clientName', 'clientType']
    prepopulated_fields = {'clientName': ('clientType',)}
    list_filter = ['clientName', 'clientType', 'clientCode']
    search_fields = ['clientName', 'clientType']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['modelnum', 'name', 'manufacturer', 'celltechnology']
    fields = ['modelnum', 'name', ('manufacturer',)]
    list_filter = ['manufacturer', 'name']
    search_fields = ['modelnum']
    prepopulated_fields = {'name': ('modelnum',)}


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['reportnum', 'issuedate', 'locationid_id', 'modelnum_id', 'standardid_id', 'userid_id']
    fields = ['reportnum', 'issuedate', 'locationid', 'modelnum', 'standardid', 'userid']
    list_filter = ['modelnum_id']
    search_fields = ['reportnum', 'issuedate', 'locationid', 'modelnum', 'standardid', 'userid']
