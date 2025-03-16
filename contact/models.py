from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    address = models.TextField()

    def __str__(self):
        return f'{self.phone_number} - {self.email}'


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    messages = models.TextField()

    def __str__(self):
        return f'{self.email} - {self.messages}'
