import math
movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies: list) -> float:
    rating = []                            # empty list of movie ratings
    for movie in movies:
        rating.append(movie["rating"])     # filling list with ratings
    avg_rating = sum(rating)/len(rating)   # count average rating
    return round(avg_rating, 1)            # return rounded to 1 digit


def catalog_age_stats(movies: list, current_year=2026) -> tuple:
    oldest = current_year - movies[0]["year"]                    # sets first movie as oldest
    newest = current_year - movies[0]["year"]                    # sets first movie as newest
    age = []                                                     # empty list for count avg
    for m in movies:
        oldest = current_year - m["year"] if oldest < current_year - m["year"] else oldest
        newest = current_year - m["year"] if newest > current_year - m["year"] else newest
        age.append(current_year - m["year"])
    avg_age = math.ceil(sum(age)/len(age))
    return (oldest, newest, avg_age)


def duration_in_hours(minutes: int) -> str:
    hours = minutes // 60
    mins = minutes % 60
    return f'{hours}ч {mins}м'


def rating_tier(rating: float) -> str:
    if rating >= 9:
        verdict = 'шедевр'
    elif 9 > rating >= 5:
        verdict = 'хорошо' if rating > 7 else 'средне'
    else:
        verdict = 'слабо'
    verdict = ('Рейтинг должен быть числом от 0 до 10'
               if rating > 10 or rating < 0 else verdict)
    return verdict


def decade_label(year):
    match year:
        case _ if year > 2026:
            return 'Ошибка! Фильм ещё не вышел в прокат!'
        case _ if year < 1888:
            return 'Ошибка! Первый фильм был снят в 1888 году!' # Roundhay Garden Scene
        case _ if 2020 <= year <= 2026:
            return 'новые'
        case _ if 2015 <= year < 2020:
            return 'недавние'
        case _:
            return 'старые'


for movie in movies:                     # entering each movie as dict one by one
    if 'comedy' not in movie['genres']:  # checking if 'comedy' is in genres
        print(movie['title'])            # print movie name if its genre not 'comedy'
    else:
        continue


mc = 0
while mc < len(movies):
    if movies[mc]['rating'] < 9:
        mc +=1
    else:
        print(f'{movies[mc]['title']} - ШЕДЕВР!')
        break                     # if rating > 9 is found, cycle breaks
else:
    print('Шедевров не найдено')  # if no rating is > 9


def count_long_movies(movies: list, threshold=120) -> int:
    mc = 0                        # movie count
    for movie in movies:
        if movie['duration_min'] > threshold:
            mc += 1
    return mc


def normalize_title(title: 'str') -> str:
    title_norm = ''
    splited = title.split(sep = ' ')
    for word in splited:
        title_norm += word[0].upper() + word[1:] + ' '
    return title_norm.strip()


def make_slug(title: 'str') -> str:
    return title.lower().replace(' ', '-')


def format_report_line(movie: dict) -> str:
    return (f'"{normalize_title(movie['title'])}"'
    f' ({movie['year']}) — {movie['rating']}/10, ' 
    f'{duration_in_hours(movie['duration_min'])}, '
    f'жанры: {', '.join(sorted(movie['genres']))}')
