import urllib.request
from pprint import pprint
import json

# python manage.py dumpdata movies.Movie --indent 4 > movies.json

API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYzZlZTRmNmMzMTYwMzgzZGYwMDNiZmRlZTJmODk1NCIsInN1YiI6IjY1M2Y2NzVkYzhhNWFjMDEzYTg3Y2Y2MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oAAfSlKU7IPIDpHjBRcgm6ELjUbc40HhWHdO7L1yI-4'
HOST = "https://api.themoviedb.org"
MOVIE_LIST_URI = "/3/movie/popular"
MOVIE_INFO_URI = "/3/movie/"
GENRE_LIST_URI = "/3/genre/movie/list"

movie_list = []
movie_Ids = []
genre_list = []

genre_request = (f'{HOST}{GENRE_LIST_URI}?api_key={API_KEY}&language=ko')
response = urllib.request.urlopen(genre_request)
json_str = response.read().decode('utf-8')
json_object = json.loads(json_str)

genre_data = json_object.get("genres")

for data in genre_data:

    my_data = {
        "number": data.get("id"),
        "name": data.get("name")
    }

    my_genre = {
        "model": "movies.genre",
        "pk": my_data.get("number"),
        "fields": {
            "name": my_data.get("name")
        },
    }
    genre_list.append(my_genre)

for i in range(1, 50):
    request = (f'{HOST}{MOVIE_LIST_URI}?api_key={API_KEY}&language=ko&page={i}')
    response = urllib.request.urlopen(request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)

    data_movies = (json_object.get("results"))

    for movie in data_movies:
        movie_Ids.append(movie.get("id"))

for idx, movie_Id in enumerate(movie_Ids):
    movie_request = (f'{HOST}{MOVIE_INFO_URI}{movie_Id}?api_key={API_KEY}&language=ko&')
    response = urllib.request.urlopen(movie_request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)
    if json_object.get("poster_path"):
        if json_object.get("genres"):
            my_object = {
                "model": "movies.movie",
                "pk": idx+1,
                "fields": {
                    "title": json_object.get("title"),
                    "release_date": json_object.get("release_date"),
                    "popularity": json_object.get("popularity"),
                    "vote_count": json_object.get("vote_count"),
                    "vote_average": json_object.get("vote_average"),
                    "overview": json_object.get("overview"),
                    "poster_path": json_object.get("poster_path"),
                    "genres": [json_object.get("genres")[0].get("id")],
                }  
            }
        else:
            my_object = {
                "model": "movies.movie",
                "pk": idx+1,
                "fields": {
                    "title": json_object.get("title"),
                    "release_date": json_object.get("release_date"),
                    "popularity": json_object.get("popularity"),
                    "vote_count": json_object.get("vote_count"),
                    "vote_average": json_object.get("vote_average"),
                    "overview": json_object.get("overview"),
                    "poster_path": json_object.get("poster_path"),
                    "genres": json_object.get("genres"),
                }
            }
        movie_list.append(my_object)

with open('movies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(movie_list, ensure_ascii=False))

with open('genres.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(genre_list, ensure_ascii=False))