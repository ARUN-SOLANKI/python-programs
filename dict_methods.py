user_info = dict(
            name = 'arun solanki',
            age = 24,
            roll_no = 1896202816,
            collage = 'dr akhilesh das fgupta institite of technology and management',
            fav_movies = ['3 idiot' , 'sanju']

)

# print(user_info)

# #  cheak for keys
# if 'collage' in user_info :
#     print("present")
# else:
#     print("not present")

# cheak for values
# if 24 in user_info.values() :
#     print("present")
# else:
#     print("not present")

# cheak for list
# if ['3 idiot' , 'sanju'] in user_info.values() :
#     print("present")
# else:
#     print("not present")

# for i in user_info.values() :
#     print(i)


#  item methodes

# user_items = user_info.items()
# print(user_items)
# print(type(user_items))


# for first , second in user_items :
#     print(f" {first} ------------ {second}")


# for first  in user_items :
#     print(f" {first} ------------ ")

# user_info.update(dict.fromkeys(['name','age'] , 'moye kha pato'))
# print(user_info.get('name', "wrong key"))
print(user_info)