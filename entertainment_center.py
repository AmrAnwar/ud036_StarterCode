# import the Movie class and open_movies_page from init.py file
from media import Movie
from fresh_tomatoes import open_movies_page


def create_movies():
    """
    create movies objects
    then send them to open_movies_page function to create the html page
    """
    Movie(
        title="Big hero 6",
        image_url="http://www6.0zz0.com/2017/09/21/19/825878595.jpg",
        youtube_url="https://www.youtube.com/watch?v=z3biFxZIJOQ")
    Movie(
        title="frozen",
        image_url="http://www9.0zz0.com/2017/09/21/19/871522439.jpg",
        youtube_url="https://www.youtube.com/watch?v=TbQm5doF_Uc")
    Movie(
        title="Kimi no na Wa(your name)",
        image_url="http://www9.0zz0.com/2017/09/21/19/467915164.jpg",
        youtube_url="https://www.youtube.com/watch?v=hRfHcp2GjVI")
    Movie(
        title="A Silent Voice",
        image_url="http://www9.0zz0.com/2017/09/21/19/194459511.jpg",
        youtube_url="https://www.youtube.com/watch?v=nfK6UgLra7g")
    Movie(
        title="spirited away",
        image_url="http://www9.0zz0.com/2017/09/21/19/974860969.jpg",
        youtube_url="https://www.youtube.com/watch?v=ByXuk9QqQkk", )
    Movie(
        title="the wind Rises",
        image_url="http://www9.0zz0.com/2017/09/21/19/474969239.jpg",
        youtube_url="https://www.youtube.com/watch?v=2QFBZgAZx7g", )

    open_movies_page(Movie.movies)


if __name__ == "__main__":
    create_movies()
