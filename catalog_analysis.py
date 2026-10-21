import math

movies = [
    {
        "title": "The Dune Chronicles", 
        "year": 2021, 
        "genres": {"sci-fi", "drama"},
        "rating": 8.6, 
        "duration_min": 155, 
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]
    },
    {
        "title": "Kitchen Stories", 
        "year": 2019, 
        "genres": {"comedy", "drama"},
        "rating": 7.1, 
        "duration_min": 98, 
        "actors": ["A. Novak", "M. Ferguson"]
    },
    {
        "title": "silent hours", 
        "year": 2016, 
        "genres": {"thriller", "drama"},
        "rating": 6.4, 
        "duration_min": 112, 
        "actors": ["J. Bloom", "K. Lee"]
    },
    {
        "title": "Comet Racers", 
        "year": 2023, 
        "genres": {"sci-fi", "action"},
        "rating": 5.9, 
        "duration_min": 101, 
        "actors": ["O. Isaac", "P. Diaz"]
    },
    {
        "title": "The Last Bakery", 
        "year": 2014, 
        "genres": {"comedy"},
        "rating": 7.8, 
        "duration_min": 89, 
        "actors": ["A. Novak", "T. Chalamet"]
    },
    {
        "title": "midnight in oslo", 
        "year": 2020, 
        "genres": {"thriller", "mystery"},
        "rating": 8.9, 
        "duration_min": 124, 
        "actors": ["K. Lee", "R. Ferguson"]
    },
    {
        "title": "Garden of Static", 
        "year": 2022, 
        "genres": {"drama"},
        "rating": 4.8, 
        "duration_min": 137, 
        "actors": ["P. Diaz", "J. Bloom"]
    },
    {
        "title": "The Quiet Algorithm", 
        "year": 2024, 
        "genres": {"sci-fi", "drama"},
        "rating": 9.2, 
        "duration_min": 118, 
        "actors": ["M. Ferguson", "O. Isaac"]
    },
    {
        "title": "Two Left Shoes", 
        "year": 2011, 
        "genres": {"comedy"},
        "rating": 6.0, 
        "duration_min": 95, 
        "actors": ["A. Novak", "K. Lee"]
    },
    {
        "title": "Red Harbor", 
        "year": 2018, 
        "genres": {"action", "thriller"},
        "rating": 7.3, 
        "duration_min": 129, 
        "actors": ["P. Diaz", "T. Chalamet"]
    },
]


def average_rating(movies):
    rating_sum = sum(mov['rating'] for mov in movies)
    total_n = len(movies)
    return round(rating_sum / total_n, ndigits=1)


def catalog_age_stats(movies, current_year=2026):
    old_movie = max(movies, key=lambda mov: current_year - mov['year'])
    new_movie = min(movies, key=lambda mov: current_year - mov['year'])

    old_movie = old_movie['year']
    new_movie = new_movie['year']

    year_sum = sum(mov['year'] for mov in movies)
    total_n = len(movies)

    mean_year = math.ceil(year_sum / total_n)

    return (old_movie, new_movie, mean_year)


def duration_in_hours(minutes):
    hours = minutes // 60
    remain_minutes = minutes % 60
    return f"{hours}ч {remain_minutes}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif 7 <= rating < 9:
        return "хорошо"
    else:
        return "средне" if 5 <= rating < 7 else "слабо"


def decade_label(year):
    match year:
        case year if year >= 2020:
            return "новые"
        case year if 2015 <= year < 2020:
            return "недавние"
        case _:
            return "старые"


def filter_non_comedy_movies(movies):
    for mov in movies:
        if 'comedy' in mov['genres']:
            continue
        print(mov['title'])


def search_first_masterpiece(movies):
    masterpiece_mov = None
    idx = 0
    while idx < len(movies):
        mov = movies[idx]
        if rating_tier(mov['rating']) == 'шедевр':
            masterpiece_mov = mov['title']
            break
        idx += 1
    else:
        return "Шедевров не найдено"
    return masterpiece_mov


def count_long_movies(movies, threshold=120):
    lm_counter = 0
    for mov in movies:
        if mov['duration_min'] > threshold:
            lm_counter += 1
    return lm_counter


def normalize_title(title):
    words = title.split()
    words = [word[0].upper() + word[1:] for word in words]
    return " ".join(words)


def make_slug(title):
    norm_title = title.lower().replace(' ', '-')
    return norm_title


def format_report_line(movie):
    output = (f'"{normalize_title(movie["title"])}" '
    f'({movie["year"]}) — {movie["rating"]}/10, '
    f'{duration_in_hours(movie['duration_min'])}, '
    f'жанры: {", ".join(sorted(movie['genres']))}')
    return output


def titles_sorted_by_rating(movies):
    temp_sorted_movies = sorted(
        movies, 
        key=lambda mov: mov['rating'],
        reverse=True)
    return [mov['title'] for mov in temp_sorted_movies]


def top_n_by_rating(movies, n=3):
    temp_sorted_movies = sorted(movies, key=lambda mov: -mov['rating'])
    return [(mov['title'], mov['rating']) for mov in temp_sorted_movies[:n]]


def count_by_genre(movies):
    counter = dict()
    for mov in movies:
        for genre in mov['genres']:
            counter[genre] = counter.get(genre, 0) + 1
    return counter


def actor_filmography(movies):
    counter = dict()

    for mov in movies:
        for actor in mov['actors']:
            counter[actor] = counter.get(actor, []) + [mov['title']]
    return counter


def list_good_films(movies):
    mean_rating = average_rating(movies)
    return {
        mov['title']: mov['rating'] 
        for mov in movies 
        if mov['rating'] > mean_rating
    }


def all_genres(movies):
    genres = set()
    for mov in movies:
        genres.update(mov['genres'])
    return genres


def common_actors(movie1, movie2):
    return set(movie1['actors']) & set(movie2['actors'])


def genres_only_in_one(movies_a, movies_b):
    movies_a_genres = all_genres(movies_a)
    movies_b_genres = all_genres(movies_b)
    return movies_a_genres - movies_b_genres


def iter_high_rated(movies, min_rating=8.0):
    for mov in movies:
        if mov['rating'] >= min_rating:
            yield mov
