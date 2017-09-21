import requests


class Movie(object):
    movies = []  # list to save the movies

    def __init__(self, title, image_url, youtube_url):
        """
        Author: AmrAnwar

        create a movie object by sending 3 parameters
        :param title: the movie title
        :param image_url: online url to image
        :param youtube_url: url to the movie trailer on youtube
        """
        self.title = title
        self.poster_image_url = check_is_url(url=image_url)
        self.trailer_youtube_url = check_is_url(url=youtube_url)
        # add the movie object to the list(movies)
        Movie.movies.append(self)


def check_is_url(url=None):
    """
     check if url is valid
    :param url: link
    :return: Errors :
        MissingSchema if the user didn't send url pattern
        ValueError if the pattern is true but the url is not valid
        if the url is valid return 200
    """
    # if the status code is 200 that mean good request
    if requests.get(url).status_code == 200:
        return url
    else:
        raise ValueError("please inter valid url")
