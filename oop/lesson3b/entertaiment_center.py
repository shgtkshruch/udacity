# import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
        "A story of a boy and his toys that come to life",
        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
        "Storyline",
        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
        "https://www.youtube.com/watch?v=-9ceBgWV8io")

shawshank = media.Movie("Shawshank Redempion",
        "Storyline",
        "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
        "https://www.youtube.com/watch?v=6hB3S9bIaco")

new_cinema = media.Movie("New Cinema Paradise",
        "Storyline",
        "http://fukushima.heim-tohoku.co.jp/blog_imgs/4/images/old/0807_20080704104717.jpg",
        "https://www.youtube.com/watch?v=C2-GX0Tltgw")

ratatouille = media.Movie("Ratacouiale",
        "Storyline", 
        "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
        "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
        "Storyline",
        "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
        "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games",
        "Storyline",
        "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
        "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, shawshank, new_cinema, ratatouille, midnight_in_paris, hunger_games]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RAITINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
