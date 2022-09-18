from django.core.validators import MinValueValidator
from django.db import models

from apps.asset.models import Asset
from apps.common.models import TimeStampedModel
from apps.user.models import User

STOCK_FIRM_CHOICES = (
    ('디셈버증권', '디셈버증권'),
    ('핀트투자증권', '핀트투자증권'),
    ('베스트투자', '베스트투자')
)


class Account(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_firm = models.CharField(max_length=30, choices=STOCK_FIRM_CHOICES)
    account_number = models.CharField(max_length=30)
    account_name = models.CharField(max_length=30)
    principal = models.DecimalField(max_digits=16, decimal_places=2, default=0, validators=[MinValueValidator(0)])


class AccountAsset(TimeStampedModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    current_price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    count = models.IntegerField(validators=[MinValueValidator(0)])


class Transaction(TimeStampedModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=16, decimal_places=2, validators=[MinValueValidator(0)])
