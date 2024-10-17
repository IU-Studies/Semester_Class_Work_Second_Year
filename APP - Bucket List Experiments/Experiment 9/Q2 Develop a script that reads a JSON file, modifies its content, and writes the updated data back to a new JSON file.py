""" Develop a script that reads a JSON file, modifies its content, and writes the updated data back to a new
JSON file. """

import json

def modify_json_data(input_file, output_file, modifications):
    with open(input_file, 'r') as infile:
        data = json.load(infile)  
        
        for key, value in modifications.items():
            if key in data:
                data[key] = value  
            else:
                data[key] = value  

    
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)  

modifications = {
    "name": "New Name",  
    "age": 30,           
    "city": "New York"   
}


input_json = "input_file.json"  
output_json = "output_file.json"  

modify_json_data(input_json, output_json, modifications)

print(f"Data from {input_json} has been modified and written to {output_json}.")
