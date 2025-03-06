from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    headers = {'id': 'ID', 
               'name': 'Название', 
               'category': 'Категория', 
               'status': 'Статус', 
               'price': 'Цена', 
               'last_month_orders': 'Заказов за последний месяц', 
               'current_month_orders': 'Заказов за текущий месяц'}
    context = {
        'headers': headers,
        'products': products,
    }

    return render(request,'index.html', context)