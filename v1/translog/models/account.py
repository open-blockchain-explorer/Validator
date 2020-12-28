from uuid import uuid4

from django.core.validators import MaxValueValidator
from django.db import models
from thenewboston.constants.network import BALANCE_LOCK_LENGTH, MAX_POINT_VALUE, VERIFY_KEY_LENGTH


class Account(models.Model):
    status_choices = [
        ('PENDING', 0),
        ('SENT', 1),
        ('REJECTED', 2)
    ]
    #id = models.UUIDField(default=uuid4, editable=False, primary_key=True)  # noqa: A003
    account_number = models.CharField(max_length=VERIFY_KEY_LENGTH, unique=True)
    balance = models.PositiveBigIntegerField(
        default=0,
        validators=[
            MaxValueValidator(MAX_POINT_VALUE)
        ]
    )
    balance_lock = models.CharField(max_length=BALANCE_LOCK_LENGTH, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=status_choices)

    class Meta:
        default_related_name = 'accounts'

    def __str__(self):
        return (
            f'Account Number: {self.account_number} | '
            f'Balance Lock: {self.balance_lock} | '
            f'Balance: {self.balance} | '
        )
