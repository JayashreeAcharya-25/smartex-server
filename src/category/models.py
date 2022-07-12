from django.db import models

# Create your models here.
class Category(models.Model):
    cat_slno = models.CharField(max_length=150)
    cat_name = models.CharField(max_length=150)
    cat_brand = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'category'
