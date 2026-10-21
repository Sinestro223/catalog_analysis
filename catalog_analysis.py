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
