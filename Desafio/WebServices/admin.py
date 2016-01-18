from django.contrib import admin
from .models import Company, Servers
# Register your models here.

class ServersInline(admin.TabularInline):
    model = Servers
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Company Information',               {'fields': ['name', 'address']}),
    ]
    inlines = [ServersInline]
    list_display = ('name', 'address')
    search_fields = ['name']

admin.site.register(Company, CompanyAdmin)
