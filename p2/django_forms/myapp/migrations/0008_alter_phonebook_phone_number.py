# Generated by Django 3.2.7 on 2021-09-16 17:38

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_phonebook_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonebook',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=12, null=True, region=None),
        ),
    ]