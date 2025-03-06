from django.core.management.base import BaseCommand, CommandError
from products.models import Product, Category
from orders.models import Order, OrderItem
from datetime import datetime
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
            
            try:
                product = Product.objects.get(name=row['name'])
                created = False
            except:
                product = Product()
                created = True
        
            product.category = row['category']
            product.status = row['status']
            product.price = row['price']
            product.name = row['name']
            product.save()

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
        data = demo.get_orders()
        for row in data:
            try:
                self.create_order(row)
            except Exception as e:
                print(e)

        
    def create_order(self, row): 
        product = Product.objects.get(
            name=row['order_item']
        )

        order, created = Order.objects.get_or_create(
            order_number=row['order_number'],
            status=row['status'],
            date=datetime.strptime(row['date'], '%d.%m.%Y'),
        )

        order_item, _ = OrderItem.objects.get_or_create(
            product=product,
            order=order,
            quantity=row['quantity']
        )

        print(f'Добавлени {order_item} в кол-ве {order_item.quantity} к заказау №{order_item.order}')