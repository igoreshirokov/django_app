from django.db import models

ORDER_STATUS = {
    'ожидание': 'В ожидании',
}

class Order(models.Model):
    status = models.CharField(max_length=50, default=ORDER_STATUS['ожидание'], choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_item')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField(default=1)
