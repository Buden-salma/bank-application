# Generated by Django 5.1.4 on 2024-12-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_alter_transaction_history_payee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_history',
            name='payee_ID',
            field=models.IntegerField(),
        ),
    ]