from django.db import models

# Create your models here.
class Brands(models.Model):
    id = models.IntegerField(primary_key=True)
    brand_slno = models.CharField(max_length=150)
    brand_name = models.CharField(max_length=150)
    brand_image = models.ImageField(upload_to = "brands/")

    class Meta:
        managed = False
        db_table = 'brands'