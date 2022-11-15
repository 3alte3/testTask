# Generated by Django 4.0.6 on 2022-11-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_transaction_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('DE', 'Debiting'), ('RE', 'Replenishment')], max_length=255, null=True),
        ),
    ]
