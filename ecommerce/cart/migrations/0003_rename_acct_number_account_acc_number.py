# Generated by Django 4.2.3 on 2023-08-06 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_account_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='acct_number',
            new_name='acc_number',
        ),
    ]
