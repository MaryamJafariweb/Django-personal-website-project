from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='services/images/')
    body = models.TextField()

    def __str__(self):
        return self.name

