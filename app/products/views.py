from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate as django_authenticate, get_user_model, login as django_login, logout as django_logout

def index(request):
    if request.user.is_authenticated:
        return table(request)
    else:
        return login(request)

def table(request):
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

def registration(request):
    return render(request, 'registration.html')

def login(request):
    message = ''
    if request.method == 'POST':
        try:
            user = authenticate(request)
            if user is not None:
                django_login(request, user)
                return table(request)        
        except Exception as e:
            message = e

    return render(request, 'login.html', {
        'message': message
    })

def logout(request):
    django_logout(request)
    return redirect('/')

def authenticate(request):
    try:
        user = get_user_model().objects.get(email=request.POST.get('email'))
        user = django_authenticate(username=user.username, password=request.POST.get('password'))
        return user
    except get_user_model().DoesNotExist:
        raise Exception('Email не зарегистрирован')
    except:
        raise Exception('Проверьте email или пароль')
