from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):  # или admin.StackedInline для другого стиля отображения
    model = OrderItem
    extra = 1  # Количество пустых форм для добавления новых OrderItem
    fields = ('product', 'quantity') 

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'status', 'date')  # Поля, отображаемые в списке заказов
    list_filter = ('status', 'date')  # Фильтры в списке заказов
    search_fields = ('order_number',)  # Поля для поиска
    inlines = [OrderItemInline]  # Вложенные инлайны для OrderItem

