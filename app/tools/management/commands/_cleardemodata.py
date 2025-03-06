from django.core.management.base import BaseCommand, CommandError
from products.models import Product, Category
from orders.models import Order, OrderItem

class Command(BaseCommand):
    help = "Добавление демо данных в базу данных"

    def add_arguments(self, parser):
        pass 
    
    def handle(self, *args, **options):
        self.delete_products()
        self.delete_categories()
        self.delete_orders()

    def delete_products(self):
        products = Product.objects.all()
        for product in products:
            name = product.name
            product.delete()
            print(f'Товар "{name}" удален')

    def delete_categories(self):
        categories = Category.objects.all()
        for category in categories:
            name = category.name
            category.delete()
            print(f'Категория "{name}" удалена')
    

    def delete_orders(self):
        """Не реализовано"""
        pass
        orders = Order.objects.all()
        for order in orders:
            order.items.all()