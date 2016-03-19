from django.contrib import admin

from main.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'iban', 'creator')

