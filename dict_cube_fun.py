# def cube_count(n) :
#     count = {}
#     for i in range(1,n+1) :
#         count[i] = i**3
#     return count

# print(cube_count(9))



# user_info = {}

# name = input("enter a name    ")
# age = int(input("enter your age    " ))
# fav_movies = input("your fav movise saprated by comma   ").split("'")
# fav_pages = input("your fav pages saprated by comma   ").split("'")


# user_info['name'] = name
# user_info['age'] = age
# user_info['fav_movies'] = fav_movies
# user_info['fav_pages'] = fav_pages


# for key , values  in user_info.items():
#     print(f"{key} : {values}")


def word_count(string1) :
    words ={}
    for char in string1 :
        words[char] = string1.count(char)
    return words

print(word_count("arun solanki"))