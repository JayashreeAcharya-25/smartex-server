from django.db import models

# Create your models here.
class Stock(models.Model):
    id: models.IntegerField(primary_key=True)
    stk_slno = models.CharField(max_length=150)
    stk_pro_id = models.IntegerField()
    stk_qty = models.IntegerField()
    stk_status = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'stock'
