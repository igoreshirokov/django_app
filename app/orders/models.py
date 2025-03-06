from django.db import models
from datetime import datetime

ORDER_STATUS = {
    'ожидание': 'В ожидании',
    'выполнен': 'Выполнен',
}

class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=50, default=ORDER_STATUS['ожидание'], choices=ORDER_STATUS)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.order_number

class OrderItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_item')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name