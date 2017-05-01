#!C:/Python27/python

from base import Movie
import json


# This method reads movies.json file. For each movie in the file it
# will create a Movie object and add it to the movies list.  This
# method will return list of movies.
def get_movies():
    with open('movies.json') as movies_file:
        data = json.load(movies_file)

    movies = []
    for movie_data in data["movies"]:
        m = Movie(
            movie_data["title"],
            movie_data["duration"],
            movie_data["trailer_youtube_url"],
            movie_data['poster_image_url'],
            movie_data['storyline'],
            movie_data['rating']
            )
        movies.append(m)
    return movies
