# Generated by Django 5.1.6 on 2025-03-06 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 6, 20, 54, 28, 518182)),
        ),
    ]
