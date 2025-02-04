movies = [ 
{ 
"name": "Usual Suspects",  
"imdb": 7.0, 
"category": "Thriller" 
}, 
{ 
"name": "Hitman", 
"imdb": 6.3, 
"category": "Action" 
}, 
{ 
"name": "Dark Knight", 
"imdb": 9.0, 
"category": "Adventure" 
}, 
{ 
"name": "The Help", 
"imdb": 8.0, 
"category": "Drama" 
}, 
{ 
"name": "The Choice", 
"imdb": 6.2, 
"category": "Romance" 
}, 
{ 
"name": "Colonia", 
"imdb": 7.4, 
"category": "Romance" 
}, 
{ 
"name": "Love", 
"imdb": 6.0, 
"category": "Romance" 
}, 
{ 
"name": "Bride Wars", 
"imdb": 5.4, 
"category": "Romance" 
}, 
{ 
"name": "AlphaJet", 
"imdb": 3.2, 
"category": "War" 
}, 
{ 
"name": "Ringing Crime", 
"imdb": 4.0, 
"category": "Crime" 
}, 
{ 
"name": "Joking muck", 
"imdb": 7.2, 
"category": "Comedy" 
}, 
{ 
"name": "What is the name", 
"imdb": 9.2, 
"category": "Suspense" 
}, 
{ 
"name": "Detective", 
"imdb": 7.0, 
"category": "Suspense" 
}, 
{ 
"name": "Exam", 
"imdb": 4.2, 
"category": "Thriller" 
}, 
{ 
"name": "We Two", 
"imdb": 7.2, 
"category": "Romance" 
} 
]


#1
def imdb(movies): 
    name = input("name:") 
    for movie in movies: 
        if movie["name"] == name: 
            if movie["imdb"] > 5.5: 
                return True 
    return False 

print(imdb(movies))

#2
def get_good_movies(movies): 
    good_movies = [movie for movie in movies if movie["imdb"] > 5.5] 
    return good_movies 

print(get_good_movies(movies))

#3
def category(movies): 
    name = input("name:") 
    result = [] 
    for movie in movies:   
        if movie["category"] == name: 
            result.append(movie) 
    return result 

print(category(movies))

#4

def avg(movies): 
    total = 0 
    cnt = 0 
    for movie in movies: 
        total += movie['imdb'] 
        cnt += 1 
    return total / cnt

print(avg(movies))

#5 
def avg_imdb_by_category(movies, category): 
    total = 0 
    cnt = 0 
    for movie in movies: 
        if movie["category"] == category: 
            total += movie["imdb"] 
            cnt += 1 
    if cnt == 0: 
        return None 
    return total / cnt 

category = input('Enter the category: ') 
print(avg_imdb_by_category(movies, category))
