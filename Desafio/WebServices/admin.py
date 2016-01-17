from django.contrib import admin
from .models import Company, Servers
# Register your models here.

class ServersInline(admin.StackedInline):
    model = Servers
    extra = 3


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['address']}),
    ]
    inlines = [ServersInline]


admin.site.register(Company, CompanyAdmin)
