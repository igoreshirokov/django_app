import os
import csv

def get_products():
    path = os.path.dirname(__file__)
    csv_file = path + '/demo.products.csv'
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

def get_orders():
    path = os.path.dirname(__file__)
    csv_file = path + '/demo.orders.csv'
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row