# Generated by Django 3.2.7 on 2021-09-16 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_phonebook_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonebook',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
