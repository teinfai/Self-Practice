# Generated by Django 3.2.7 on 2021-09-16 14:41

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_phonebook_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonebook',
            name='phonenumber',
        ),
        migrations.AlterField(
            model_name='phonebook',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=100, region=None),
        ),
    ]
