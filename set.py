set_demo ={1,2,3,4}
# print(set_demo)
# print(set_demo[1])  # error

# if 6 in set_demo :
#     print("presents")
# else:    
#     print("not presents")



# for i in set_demo :
#     print(i)
# print(set_demo)

# list_demo = [1,2,3,4,5,6,7,8,9,1,2,5,4,3,6,8,2]
# convert_into_set = list(set(list_demo))
# print(list_demo)
# print(convert_into_set)

# set methods

# set_demo.add(6)
# set_demo.add(7)
# set_demo.add(2)
# set_demo.add(5)

# set_demo.remove(5)
# set_demo.remove(9)
# set_demo.discard(9)
# set_demo.discard(1)

# s1 = set_demo.copy()

# print(s1)
# print(set_demo)

#  set is an unordered collaction of data
# it can not store list and disctionary

# set maths

set1 = {1,2,3,4,5}
set2 = {1,2,3,5,6,8}

union = set1 | set2
print(union)

intersection = set1 & set2
print(intersection)
