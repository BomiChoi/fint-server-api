from django.db import models

ASSET_GROUP_CHOICES = (
    ('미국 주식', '미국 주식'),
    ('미국섹터 주식', '미국섹터 주식'),
    ('선진국 주식', '선진국 주식'),
    ('신흥국 주식', '신흥국 주식'),
    ('전세계 주식', '전세계 주식'),
    ('부동산 / 원자재', '부동산 / 원자재'),
    ('채권 / 현금', '채권 / 현금')
)


class Asset(models.Model):
    asset_name = models.CharField(max_length=30)
    isin = models.CharField(max_length=12)
    asset_group = models.CharField(max_length=30, choices=ASSET_GROUP_CHOICES)
