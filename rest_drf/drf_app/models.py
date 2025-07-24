from django.db import models


class TwoWheelar(models.Model):
    reg_no = models.CharField(max_length=8, primary_key=True)
    bike_model = models.CharField(max_length=40, blank=False, null= False)
    purchase_date = models.DateField()
    brand = models.CharField(max_length= 20, )
    cost = models.FloatField()


