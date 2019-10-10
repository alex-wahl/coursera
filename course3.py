import json
import requests_with_caching
    
def get_movies_from_tastedive (obj):
    url = "https://tastedive.com/api/similar"
    
    params = {
        "q": obj,
        "type": "movies",
        "limit":"5"
    }
    r = requests_with_caching.get(url, params = params)
    response = json.loads(r.text)
    movies = response
    return movies


def extract_movie_titles(dic):
    obj = dic['Similar']['Results']
    titles = []
    for i in obj:
        titles.append(i['Name'])
    return titles


def get_related_titles(titles):
    url = "https://tastedive.com/api/similar"
    related_titles = []
    for i in titles:
        params = {
            "q": i,
            "type": "movies",
            "limit":"5"
        }
        r = requests_with_caching.get(url, params = params)
        try:
            resp = json.loads(r.text)
            for i in resp['Similar']['Results']:
                if i['Name'] not in related_titles:
                    related_titles.append(i['Name'])
        except:
            pass
    return related_titles


def get_movie_data(title):
    url = "http://www.omdbapi.com/"
    params = {
        "t": title,
        "r": "json"
    }
    
    r = requests_with_caching.get(url, params = params)
    movie = json.loads(r.text)
    return movie
    

def get_movie_rating (movie):
    ratings = movie['Ratings']
    find = False
    rating = 1
    for sources in ratings:
        for k,v in sources.items():
            if v == "Rotten Tomatoes":
                find = True
            if "%" in v:
                rating = int(str(v[:2]))
    if find == True:
        return rating
    else:
        return 0
                
def get_sorted_recommendations (titles):
    related_titles = get_related_titles(titles) #list
    moviesrating = []
    for i in related_titles:
        get_ranking = get_movie_data(i)
        rating = get_movie_rating(get_ranking)
        moviesrating.append(rating)
    mrating = sorted(zip(related_titles, moviesrating))
    y = sorted(mrating, key=lambda rating: rating[1], reverse=True)
    sortedlist = []
    for (movie, ranking) in y:
      sortedlist.append(movie)
    print(sortedlist)
    return sortedlist

movies = get_movies_from_tastedive ("Bridesmaids")
titles = extract_movie_titles(movies)
#related_titles = get_related_titles(titles)
sorted_recommendations = get_sorted_recommendations(titles)
