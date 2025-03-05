from django.db import models

PRODUCT_STATUS = {
    "publish": "Опубликован",
    "draft": "Черновик",
}

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    status = models.CharField(choices=PRODUCT_STATUS, default=PRODUCT_STATUS["draft"], max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    def countOrdersLastMonth(self):
        pass

    def countOrdersCurrentMonth(self):
        pass




