# THIS CODE FILTERS THE 1 DAY DELIVERIES AND PRINTS THEM
import csv

FILE = 'MOCK_DATA.csv'

def file_manager(file):
    deliveries = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            if line['Shipping Time'] == '1':
                order_id = line['first_name']
                first_name = line['order_id']
                shipping_address = line['Shipping Address']

                delivery = (order_id, first_name, shipping_address)
                deliveries.append(delivery)
    return deliveries

print(file_manager(FILE))