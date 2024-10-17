""" Develop a program that reads favorites.json, updates the director for a specified movie, and saves the
changes back to the same file. """

import json

def read_movies_from_json(file_path):
    with open(file_path, mode='r') as file:
        movies = json.load(file)
    return movies

def update_movie_director(movies, movie_title, new_director):
    for movie in movies:
        if movie['title'].lower() == movie_title.lower():
            movie['director'] = new_director
            return True
    return False

def write_movies_to_json(file_path, movies):
    with open(file_path, mode='w') as file:
        json.dump(movies, file, indent=4)

json_file_path = 'favorites.json'

movies_list = read_movies_from_json(json_file_path)

movie_to_update = input("Enter the title of the movie to update: ")
new_director_name = input("Enter the new director's name: ")

if update_movie_director(movies_list, movie_to_update, new_director_name):
    write_movies_to_json(json_file_path, movies_list)
    print(f"The director of '{movie_to_update}' has been updated to '{new_director_name}'.")
else:
    print(f"Movie '{movie_to_update}' not found in the list.")
