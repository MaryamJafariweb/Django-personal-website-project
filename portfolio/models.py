from django.db import models

# Create your models here.

class Portfolio(models.Model):
    banner = models.ImageField(upload_to="portfolio/banner")
    title = models.CharField(max_length=100)
    image1 =  models.ImageField(upload_to="portfolio/image", null = True, blank=True)
    image2 =  models.ImageField(upload_to="portfolio/image", null = True, blank=True)
    image3 =  models.ImageField(upload_to="portfolio/image", null = True, blank=True)
    image4 =  models.ImageField(upload_to="portfolio/image", null = True, blank=True)
    description = models.TextField()
    summery = models.TextField()
    designer = models.TextField()

    def __str__(self):
        return self.title
