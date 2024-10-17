"""Create a script that collects user input for a list of products (name, price, quantity) and writes this data to a
new CSV file named products.csv."""

import csv

def collect_product_data():
    products = []
    
    while True:
        name = input("Enter product name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        
        price = input("Enter product price: ")
        quantity = input("Enter product quantity: ")

        products.append((name, price, quantity))

    return products

def write_products_to_csv(file_path, products):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
      
        writer.writerow(['Name', 'Price', 'Quantity'])
        
        writer.writerows(products)

product_list = collect_product_data()

csv_file_path = 'products.csv'

write_products_to_csv(csv_file_path, product_list)

print(f"Product data has been written to {csv_file_path}.")
