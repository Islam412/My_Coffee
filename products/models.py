from django.db import models
from datetime import datetime
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=20000)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    image = models.ImageField('photos/%y%m%d')
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-publish_date']
