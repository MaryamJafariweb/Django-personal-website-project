from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    description = models.TextField()
    resume = models.FileField(upload_to='resume')

    def __str__(self):
        return self.name
