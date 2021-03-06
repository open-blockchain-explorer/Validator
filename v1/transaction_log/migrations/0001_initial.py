# Generated by Django 3.1.3 on 2020-12-29 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=64)),
                ('recipient', models.CharField(max_length=64)),
                ('balance_lock', models.CharField(max_length=64, unique=True)),
                ('amount', models.PositiveBigIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(281474976710656)])),
                ('bank_account', models.CharField(max_length=64)),
                ('bank_fee', models.PositiveBigIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(281474976710656)])),
                ('validator_account', models.CharField(max_length=64)),
                ('validator_fee', models.PositiveBigIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(281474976710656)])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('signature', models.CharField(max_length=128)),
                ('status', models.IntegerField(choices=[('UNCONFIRMED', 0), ('CONFIRMED', 1), ('REJECTED', 2)], default=0)),
            ],
        ),
    ]
