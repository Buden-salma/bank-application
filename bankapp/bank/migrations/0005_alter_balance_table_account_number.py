# Generated by Django 5.1.4 on 2024-12-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_alter_balance_table_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance_table',
            name='Account_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
