# Generated by Django 4.1 on 2022-09-20 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_transaction_user_alter_account_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountasset',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='account.account'),
        ),
    ]
