import os
from datetime import datetime

import django
import pandas
from apscheduler.schedulers.background import BackgroundScheduler
from django.contrib.auth.hashers import make_password
from django.db import transaction


def start():
    """ 스케줄러에 작업을 등록한 후 실행합니다. """

    scheduler = BackgroundScheduler()
    # scheduler.add_job(check_current_time, 'interval', seconds=1)
    scheduler.add_job(update_data, 'cron', hour=0)
    scheduler.start()


def check_current_time():
    """ 현재 시간을 출력합니다. """

    print("Now : %s" % datetime.now())


@transaction.atomic()
def update_data():
    """ 엑셀 파일로부터 데이터를 읽어 DB에 저장합니다. """

    from apps.account.models import Account, AccountAsset
    from apps.asset.models import Asset
    from apps.user.models import User

    asset_group_info_set = pandas.read_excel('data/asset_group_info_set.xlsx')
    account_asset_info_set = pandas.read_excel('data/account_asset_info_set.xlsx')
    account_basic_info_set = pandas.read_excel('data/account_basic_info_set.xlsx')

    for i, row in asset_group_info_set.iterrows():
        print(i)
        Asset.objects.get_or_create(
            isin=row['ISIN'],
            defaults={
                'asset_name': row['종목명'],
                'asset_group': row['자산그룹']
            }
        )

    for i, row in account_asset_info_set.iterrows():
        print(i)
        user, created = User.objects.get_or_create(
            name=row['고객이름'],
            defaults={
                'username': 'user' + str(i).zfill(4),
                'password': make_password('testtest')
            }
        )

        account, created = Account.objects.get_or_create(
            account_number=row['계좌번호'],
            defaults={
                'user': user,
                'stock_firm': row['증권사'],
                'account_name': row['계좌명']
            }
        )

        asset = Asset.objects.get(isin=row['ISIN'])
        AccountAsset.objects.get_or_create(
            account=account,
            asset=asset,
            defaults={
                'current_price': row['현재가'],
                'count': row['보유수량']
            }
        )

    for i, row in account_basic_info_set.iterrows():
        print(i)
        account = Account.objects.get(account_number=row['계좌번호'])
        account.principal = int(row['투자원금'])
        account.save()


if __name__ == '__main__':
    # django 환경 로드
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
    django.setup()

    update_data()
