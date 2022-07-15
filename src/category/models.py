from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    cat_slno = models.CharField(max_length=150)
    cat_name = models.CharField(max_length=150)
    cat_brand = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'category'
