# Generated by Django 2.2.24 on 2025-04-17 09:04

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20250417_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='phonenumber',
        ),
        migrations.AlterField(
            model_name='owner',
            name='pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region='RU', verbose_name='Номер владельца'),
        ),
    ]
