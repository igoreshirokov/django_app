# import debugpy

# # Ждем подключения отладчика
# debugpy.listen(('0.0.0.0', 5678))
# print("Ожидание подключения отладчика...")
# debugpy.wait_for_client()  # Остановка выполнения до подключения отладчика

# print("Отладчик подключен!")

from django.core.management.base import BaseCommand, CommandError
from products.models import Product, Category
from orders.models import Order, OrderItem
import time
from tools.data import demo

class Command(BaseCommand):
    help = "Добавление демо данных в базу данных"

    def add_arguments(self, parser):
        pass 
    
    def handle(self, *args, **options):
        self.create_products()
        self.create_orders()

    def create_products(self):
        data = demo.get_products()

        for row in data:
            row['category'] = self.create_category(row['category'])
            product, created = Product.objects.update_or_create(row)
            
            if created:
                message = f'Товар "{product.name}" создан'
            else:
                message = f'Товар "{product.name}" обновлен'

            print(message)
        
    def create_category(self, name):
        category, created = Category.objects.get_or_create(name=name)
        
        if created:
            message = f'Категория "{category.name}" создана'
        else:
            message = f'Категория "{category.name}" обновлена'
        
        print(message)

        return category

    def create_orders(self):
        pass