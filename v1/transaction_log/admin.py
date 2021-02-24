from django.contrib import admin

from .models.transaction_log import TransactionLog

admin.site.register(TransactionLog)
