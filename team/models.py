from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

role_choices = (
    ('R', 'Regular'),
    ('A', 'Admin')
)


class Member(models.Model):
    firstName = models.CharField(blank=False, max_length=40)
    lastName = models.CharField(blank=True, null=True, max_length=40)
    phoneNumber = PhoneNumberField()
    email = models.EmailField(max_length=240, blank=False)
    role = models.CharField(max_length=1, default='R', choices=role_choices)
