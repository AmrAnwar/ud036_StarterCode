from __future__ import absolute_import

from ud036_StarterCode import Movie
from ud036_StarterCode import open_movies_page


def create_movies():
    Movie(title="Big hero 6",
          image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMDliOTIzNmUtOTllOC00NDU3LWFiNjYtMGM0NDc1YTMxNjYxXkEyXkFqcGdeQXVyNTM3NzExMDQ@._V1_UY268_CR3,0,182,268_AL_.jpg",
          youtube_url="https://www.youtube.com/watch?v=z3biFxZIJOQ")
    Movie(title="frozen",
          image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
          youtube_url="https://www.youtube.com/watch?v=TbQm5doF_Uc")
    Movie(title="Kimi no na Wa(your name)",
          image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BODRmZDVmNzUtZDA4ZC00NjhkLWI2M2UtN2M0ZDIzNDcxYThjL2ltYWdlXkEyXkFqcGdeQXVyNTk0MzMzODA@._V1_UX182_CR0,0,182,268_AL_.jpg",
          youtube_url="https://www.youtube.com/watch?v=hRfHcp2GjVI")

    open_movies_page(Movie.movies)


if __name__ == "__main__":
    create_movies()
