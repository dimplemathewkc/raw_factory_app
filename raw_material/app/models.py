from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Item(TimeStamp):
    item_name = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name


class Quantity(TimeStamp):
    QUANTITY_TYPE = (
        ('oz', 'OZ'),
        ('l', 'L'),
        ('ml', 'ML'),
        ('kg', 'KG'),
    )
    amount = models.FloatField()
    quantity_type = models.CharField(choices=QUANTITY_TYPE,
                                     default='oz', max_length=4)

    def __str__(self):
        return str(self.amount)


class Inventory(TimeStamp):
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)
    price = models.FloatField()
    unit = models.IntegerField()