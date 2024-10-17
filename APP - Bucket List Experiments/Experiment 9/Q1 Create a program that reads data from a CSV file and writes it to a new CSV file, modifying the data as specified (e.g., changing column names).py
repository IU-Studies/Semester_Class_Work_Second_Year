""" Create a program that reads data from a CSV file and writes it to a new CSV file, modifying the data as
specified (e.g., changing column names). """

import csv

def modify_csv_data(input_file, output_file, column_modifications):
    with open(input_file, mode='r') as infile:
        reader = csv.DictReader(infile)

        fieldnames = reader.fieldnames
        modified_fieldnames = [column_modifications.get(name, name) for name in fieldnames]

        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=modified_fieldnames)

            writer.writeheader()

            for row in reader:
                modified_row = {column_modifications.get(k, k): v for k, v in row.items()}
                writer.writerow(modified_row)

column_changes = {
    "OldColumnName1": "NewColumnName1",
    "OldColumnName2": "NewColumnName2"
}

input_csv = "input_file.csv"  
output_csv = "output_file.csv"  

modify_csv_data(input_csv, output_csv, column_changes)

print(f"Data from {input_csv} has been modified and written to {output_csv}.")
