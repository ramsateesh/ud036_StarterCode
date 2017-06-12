# ud036_StarterCode
Source code for a Movie Trailer website.

# Pre-requisites

Install Apache and configure python 2.7.  Please see [Apache Documentation](https://httpd.apache.org/docs/2.4/platform/windows.html) for installing apache server on windows.

# Install

Go to [ud036_StarterCode](https://github.com/ramsateesh/ud036_StarterCode) and clone to your apache htdocs folder.  Rename the folder ud036_StarterCode to movies.

# Quickstart

### Get a list of movies

[Movies](http://localhost/movies) will open up list of movies that are listed in your movies.json file.

### Add more Movies to list

Use your choice of text editor to add few more movies into the json file.  Now click [Movies](http://localhost/movies) to see new list

#### movies.json

Below is the structre of a movie json.  Please not that the rating should be among the list provided.

```
{
    "title":"Movie Title",
    "duration":"Duration in Hours and Minutes eg. 2 hrs 30 mins.",
    "trailer_youtube_url":"Youtube Trailer URL",
    "poster_image_url":"Poster URL",
    "storyline":"Story line of the movie",
    "rating":"shoudl be from the list of ["G", "PG", "PG-13", "R"].  Otherwise movies.py will throw an error."
}
```

### License

`ud036_StarterCode` is a sample movie trailer website. I love open source software!  You can do what ever you want to do with this source code.
