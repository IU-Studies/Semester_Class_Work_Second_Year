""" Implement a program that searches for a specific product in products.csv based on user input and displays
the product's details if found. """

import csv

def search_product(file_path, product_name):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['name'].lower() == product_name.lower():
                return row
    return None

csv_file_path = 'products.csv'

product_to_search = input("Enter the product name to search for: ")

product_details = search_product(csv_file_path, product_to_search)

if product_details:
    print("Product found!")
    print("Name:", product_details['name'])
    print("Price:", product_details['price'])
    print("Quantity:", product_details['quantity'])
else:
    print(f"Product '{product_to_search}' not found.")
