""" Write a program that reads a JSON file containing user profiles and prints each user's name and email
address to the console. """

import json

def read_user_profiles(file_path):
    with open(file_path, mode='r') as file:
        users = json.load(file)

        for user in users:
            name = user.get('name')  
            email = user.get('email')  
            print("Name:", name)
            print("Email:", email)
            print()  

json_file_path = 'user_profiles.json'

read_user_profiles(json_file_path)
