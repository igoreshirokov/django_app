from django.db import models
from django.db.models import Sum
from datetime import datetime, timedelta

PRODUCT_STATUS = {
    "publish": "Опубликован",
    "draft": "Черновик",
}

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    status = models.CharField(choices=PRODUCT_STATUS, default=PRODUCT_STATUS["draft"], max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    def totalQuantity(self):
        return self.order_item.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0

    def countOrdersLastMonth(self):
        """Количество quantity за предыдущий месяц"""
        now = datetime.now()
        first_day_of_previous_month = (now.replace(day=1) - timedelta(days=1)).replace(day=1)
        last_day_of_previous_month = (now.replace(day=1) - timedelta(days=1))

        return self.order_item.filter(
            order__date__gte=first_day_of_previous_month,
            order__date__lte=last_day_of_previous_month
        ).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0

    def countOrdersCurrentMonth(self):
        """Количество quantity за текущий месяц"""
        now = datetime.now()
        first_day_of_current_month = now.replace(day=1)
        last_day_of_current_month = (now.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)

        return self.order_item.filter(
            order__date__gte=first_day_of_current_month,
            order__date__lte=last_day_of_current_month
        ).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0




