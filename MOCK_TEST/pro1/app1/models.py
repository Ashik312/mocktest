from django.db import models

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=20)
    product_desc = models.CharField(max_length=200)
    product_img = models.ImageField(upload_to='proimg')