from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate as django_authenticate, get_user_model, login as django_login, logout as django_logout
from django.core.validators import validate_email

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


def registration(request):
    message = ''
    if request.method == 'POST':
        try:
            user = user_registration(request)
            if user is not None:
                django_login(request, user)
                return redirect('/')
            else:
                message = "Непредвиденная ошибка"
        except Exception as e:
            message = e
    
    return render(request, 'registration.html', {
        'message': message
    })

def user_registration(request):
    email = request.POST.get('email')
    username = email.split('@')[0]
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    if password != confirm_password:
        raise Exception('Пароли не совпадают')

    try:
        validate_email(email)
    except:
        raise Exception('Введите email адрес в формате example@domain.com')
    
    User = get_user_model()

    user = None
    try:
        user = User.objects.get(email=email)
    except:
        pass

    if user is not None:
        raise Exception('Пользователь уже зарегистрирован. Пробуйте другой email адрес')

    user = User()
    user.username = username
    user.email = email
    user.set_password(password)
    user.save()

    return user

def authenticate(request):
    try:
        user = get_user_model().objects.get(email=request.POST.get('email'))
        user = django_authenticate(username=user.username, password=request.POST.get('password'))
        return user
    except get_user_model().DoesNotExist:
        raise Exception('Email не зарегистрирован')
    except:
        raise Exception('Проверьте email или пароль')
