from django.core.validators import MaxValueValidator
from django.db import models
from ...accounts.models.account import Account
from thenewboston.constants.network import BALANCE_LOCK_LENGTH, MAX_POINT_VALUE, VERIFY_KEY_LENGTH
from datetime import datetime, timedelta


class tnb_faucet(models.Model):
    social_types = [
        ('twitter', 'twitter'),
        ('facebook', 'facebook')
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    social_username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    next_valid_access_time = models.DateTimeField(default=datetime.now()+timedelta(hours=3))
    social_type = models.CharField(max_length=8, choices=social_types)

    def __str__(self):
        return (
            f'To {self.account} '
            f'using {self.social_type} | '
            f'@ {self.social_username} | '
        )
