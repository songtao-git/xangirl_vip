from django.db import models

# Create your models here.
class PurchaseOrder(models.Model):
    number = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['-create_time']


class Pick(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder)
    pick_no = models.CharField(max_length=30, primary_key=True)
    pick_type = models.CharField(max_length=30)
    warehouse = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)