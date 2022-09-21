from django.contrib import admin

from .models import Account, AccountAsset, Deposit


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'stock_firm',
        'account_number',
        'account_name',
        'principal',
        'created_at',
        'updated_at'
    )


@admin.register(AccountAsset)
class AccountAssetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'account',
        'asset',
        'current_price',
        'count',
        'created_at',
        'updated_at',
    )


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'account',
        'transfer_amount',
        'status',
        'created_at',
        'updated_at',
    )
