from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name



class Phonebook(models.Model):
    name = models.CharField(max_length=100)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,12}$")
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)

    def __str__(self):
        return self.name