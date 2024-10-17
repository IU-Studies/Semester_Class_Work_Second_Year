""" Create a script that reads a JSON file containing product information and filters out products that are
below a specified price, saving the results to a new JSON file. """

import json

def filter_products_by_price(input_file, output_file, min_price):
    try:
        with open(input_file, 'r') as infile:
            products = json.load(infile)
        
        filtered_products = [product for product in products if product['price'] >= min_price]

        with open(output_file, 'w') as outfile:
            json.dump(filtered_products, outfile, indent=4)
        
        print(f"Filtered products saved to {output_file}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except json.JSONDecodeError:
        print(f"Error reading {input_file}, please check if it's a valid JSON file.")

input_json = 'products.json'  
output_json = 'filtered_products.json'  

min_price = float(input("Enter the minimum price to filter products: "))

filter_products_by_price(input_json, output_json, min_price)
