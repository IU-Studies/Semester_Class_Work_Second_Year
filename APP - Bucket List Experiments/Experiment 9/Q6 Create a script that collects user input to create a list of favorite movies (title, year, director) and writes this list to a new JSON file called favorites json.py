""" Create a script that collects user input to create a list of favorite movies (title, year, director) and writes this
list to a new JSON file called favorites.json. """

import json

def collect_favorite_movies():
    movies = []
    
    while True:
        title = input("Enter movie title (or type 'done' to finish): ")
        if title.lower() == 'done':
            break
        
        year = input("Enter release year: ")
        director = input("Enter movie director: ")

        movies.append({
            'title': title,
            'year': year,
            'director': director
        })

    return movies

def write_movies_to_json(file_path, movies):
    with open(file_path, mode='w') as file:
        json.dump(movies, file, indent=4)

favorite_movies = collect_favorite_movies()

json_file_path = 'favorites.json'

write_movies_to_json(json_file_path, favorite_movies)

print(f"Favorite movies have been written to {json_file_path}.")
