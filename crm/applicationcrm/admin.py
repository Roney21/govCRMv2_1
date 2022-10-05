from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ['email']
    search_fields = ['email']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ()

admin.site.register(Account, AccountAdmin)
