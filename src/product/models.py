from django.db import models
from django.core.files.storage import FileSystemStorage

from mysite.settings import MEDIA_ROOT

upload_storage = FileSystemStorage(location=MEDIA_ROOT, base_url='media/')

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    pro_slno = models.CharField(max_length=150)
    pro_code = models.CharField(max_length=150)
    pro_name = models.CharField(max_length=200)
    pro_image = models.ImageField(upload_to = "products/",storage=upload_storage, null=True)
    pro_desc = models.CharField(max_length=3000)
    pro_brand = models.CharField(max_length=150)
    pro_category = models.CharField(max_length=150)
    pro_color = models.CharField(max_length=500)
    pro_qty = models.IntegerField()
    pro_sgst = models.DecimalField(max_digits=16, decimal_places=0)
    pro_cgst = models.DecimalField(max_digits=16, decimal_places=0)
    pro_price = models.DecimalField(max_digits=16, decimal_places=0)
    uid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product'
