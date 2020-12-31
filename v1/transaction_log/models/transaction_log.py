from django.core.validators import MaxValueValidator
from django.db import models
from thenewboston.constants.network import BALANCE_LOCK_LENGTH, MAX_POINT_VALUE, VERIFY_KEY_LENGTH


class TransactionLog(models.Model):
    status_choices = [
        ('UNCONFIRMED', '0'),
        ('CONFIRMED', '1'),
        ('REJECTED', '2')
    ]
    sender = models.CharField(max_length=VERIFY_KEY_LENGTH)
    recipient = models.CharField(max_length=VERIFY_KEY_LENGTH)
    balance_lock = models.CharField(max_length=BALANCE_LOCK_LENGTH, unique=True)
    amount = models.PositiveBigIntegerField(
        default=0,
        validators=[
            MaxValueValidator(MAX_POINT_VALUE)
        ]
    )
    bank_account = models.CharField(max_length=VERIFY_KEY_LENGTH)
    bank_fee = models.PositiveBigIntegerField(
        default=0,
        validators=[
            MaxValueValidator(MAX_POINT_VALUE)
        ]
    )
    validator_account = models.CharField(max_length=VERIFY_KEY_LENGTH)
    validator_fee = models.PositiveBigIntegerField(
        default=0,
        validators=[
            MaxValueValidator(MAX_POINT_VALUE)
        ]
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    signature = models.CharField(max_length=128)
    status = models.CharField(max_length=11, choices=status_choices, default=0)

    def __str__(self):
        return (
            f'{self.sender} '
            f'to {self.recipient} | '
            f'TNBC {self.amount} | '
        )
