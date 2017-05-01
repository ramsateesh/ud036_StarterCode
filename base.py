#!C:/Python27/python

# Defining a Super class Video
class Video(object):
    __doc__ = """Provides a way to store Video related information."""
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_info(self):
        print("Title: %s" % self.title)
        print("Duration: %s" % self.duration)

# Defining a sub class of Video, TvShow
class TvShow(Video):
    __doc__ = """Provides a way to store TV Show related information."""
    
    def __init__(self, title, duration,
                 season, episode, tv_station):
        super(TvShow, self).__init__(title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

# Defining a sub class of Video, Movie
class Movie(Video):
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    __doc__ = """Provides a way to store Movie related information."""
        
    def __init__(self, title, duration, trailer_youtube_url,
                 poster_image_url, storyline=None,
                 rating=None, reviews=[]):
        super(Movie, self).__init__(title, duration)
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.reviews = reviews
        self.storyline = storyline
        
        # If rating is invalid then throw a value error.
        if rating in Movie.VALID_RATINGS:
            self.rating = rating
        else:
            raise ValueError("""Invalid Rating:Rating should one of [""" +
                             ','.join(Movie.VALID_RATINGS) + "]")
