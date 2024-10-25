from bs4 import BeautifulSoup
import requests

'''Movie title - page 1'''
# page_to_scrape = requests.get("https://www.rottentomatoes.com/browse/movies_in_theaters/")
# soup = BeautifulSoup(page_to_scrape.text, "html.parser")
# movie_titles = soup.find_all("span", attrs={"class":"p--small"})
# ratings = soup.find_all("span", attrs={"class":"percentage"}) 
# release_dates = soup.find_all("span", attrs={"class":"smaller"}) 


# for title, date in zip(movie_titles, release_dates):
#     print("Title: ", title.text)
#     print("Release Date: ", date.text)


# for rating in ratings:
#     print(rating.text)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

'''Top Movies'''

# page_to_scrape = requests.get("https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page=4")
# soup = BeautifulSoup(page_to_scrape.text, "html.parser")
# movie_titles = soup.find_all("span", attrs={"class":"p--small"})
# ratings = soup.find_all("span", attrs={"class":"percentage"}) 
# release_dates = soup.find_all("span", attrs={"class":"smaller"})

# for title, date in zip(movie_titles, release_dates):
#     print("Title: ", title.text.strip())
#     print("Release Date: ", date.text.strip())
#     print("")

# for rating in ratings:
#     print(rating.numbers)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

'''Different Genres'''
# def search_movies(query):
#     Genre_page = requests.get(f"https://www.rottentomatoes.com/browse/movies_at_home/genres:{query}")
#     soup = BeautifulSoup(Genre_page.text, "html.parser")
#     movie_titles = soup.find_all("span", attrs={"class":"p--small"})
#     ratings = soup.find_all("span", attrs={"class":"percentage"}) 
#     release_dates = soup.find_all("span", attrs={"class":"smaller"})

#     moive_info = []
#     for title, date in zip(movie_titles, release_dates):
#         moive_info.append(title.text.strip() + ' : ' + date.text.strip())
    
#     for i in moive_info[4:9]:
#         print(i)

# user_input = input("Genre: ")
# search_movies(user_input)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

'''Different Genres by Platform'''
# def search_movies(genre, platform):
#     Genre_page = requests.get(f"https://www.rottentomatoes.com/browse/movies_at_home/affiliates:{platform}~genres:{genre}")
#     soup = BeautifulSoup(Genre_page.text, "html.parser")
#     movie_titles = soup.find_all("span", attrs={"class":"p--small"})
#     release_dates = soup.find_all("span", attrs={"class":"smaller"})

#     moive_info = []
#     for title, date in zip(movie_titles, release_dates):
#         moive_info.append(title.text.strip() + ' : ' + date.text.strip())
    
#     for i in moive_info[4:11]:
#         print(i)

# genre_input = input("Genre: ")
# platform_input = input("Platform: ")
# search_movies(genre_input, platform_input)

'''Different gernes by rating and platform'''

'''Different Genres by Platform'''
# def search_movies(genre, platform, ratings, amount):
#     Genre_page = requests.get(f"https://www.rottentomatoes.com/browse/movies_at_home/affiliates:{platform}~genres:{genre}~ratings:{ratings}")
#     soup = BeautifulSoup(Genre_page.text, "html.parser")
#     movie_titles = soup.find_all("span", attrs={"class":"p--small"})
#     release_dates = soup.find_all("span", attrs={"class":"smaller"})

#     moive_info = []
#     for title, date in zip(movie_titles, release_dates):
#         moive_info.append(title.text.strip() + ' : ' + date.text.strip())
    
#     for i in moive_info[0:(amount+4)]:
#         print(i)


# genre_input = input("Genre: ")
# platform_input = input("Platform: ")
# Rating_input = input("Rating: ")
# amount = int(input("Number of Movies: "))
# search_movies(genre_input, platform_input, Rating_input, amount)

'''ALL'''

Genre_List = ['Action', 'Adventure', 'Animation', 'Anime', 'Biography', 'Comedy', 'Crime', 'Documentary']

def search_movies(Question):
    if Question == "Genre":
        print("Genre Example: Action, Adventure, Animation, Anime, Biography, Comedy, Crime, Documentary")
        genre = input("Genre: ")
        if genre not in Genre_List:
            # print( "Genre Not Available")
            return "Genre Not Available"
        amount = int(input("Number of Movies: "))
        url = requests.get(f"https://www.rottentomatoes.com/browse/movies_at_home/genres:{genre}")

    elif Question == "Platform":
        print("Platform Example: Netflix, amazon_prime, showtime, vudu, peacock, hulu, disney_plus")
        platform = input("Platform: ")
        amount = int(input("Number of Movies: "))
        url = requests.get(f"https://www.rottentomatoes.com/browse/movies_at_home/affiliates:{platform}")

    elif Question == "Ratings":
        print("Rating Example: G, PG, PG-13, R, NC-17, NOT RATED, UNRATED")
        Rating = input("Rating: ")
        amount = int(input("Number of Movies: "))
        url = requests.get(f"https://www.rottentomatoes.com/browse/movies_at_home/ratings:{Rating}")

    elif Question == "All":
        genre = input("Genre: ")
        platform = input("Platform: ")
        Rating = input("Rating: ")
        amount = int(input("Number of Movies: "))
        url = requests.get(f"https://www.rottentomatoes.com/browse/movies_at_home/affiliates:{platform}~genres:{genre}~ratings:{Rating}")
                           
    soup = BeautifulSoup(url.text, "html.parser")
    movie_titles = soup.find_all("span", attrs={"class":"p--small"})
    release_dates = soup.find_all("span", attrs={"class":"smaller"})

    moive_info = []
    for title, date in zip(movie_titles, release_dates):
        moive_info.append(title.text.strip() + ' : ' + date.text.strip())
    
    for i in moive_info[4:(amount+4)]:
        print(i)
    # return moive_info
        

print("Available Criterias are:")
print("Genre")
print("Platform")
print("Ratings")
print("All")
print('')

Question = input("By which criteria you want to search: ")

print(search_movies(Question))

# print("Genre Example: Action, Adventure, Animation, Anime, Biography, Comedy, Crime, Documentary")

# print("Rating Example: G, PG, PG-13, R, NC-17, NOT RATED, UNRATED")

# print("Platform Example: Netflix, amazon_prime, showtime, vudu, peacock, hulu, disney_plus")
