from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    picture = models.ImageField(upload_to='products/')
    desc = models.TextField(max_length=500, null = True, blank=True)

    def __str__(self):
        return f"Product : {self.name.capitalize()} for Rs.{self.price}"