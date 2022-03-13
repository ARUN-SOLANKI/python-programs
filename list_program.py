# # def reverse_list(list1) :
# #     list2 = []
# #     for i in list1 :
# #         item = list1[-i]
# #         list2.append(item) 
# #     return list2

# def reverse_list(l) :
#     r_list = []
#     for i in range(len(l)) :
#         item = l.pop()
#         r_list.append(item)
#     return r_list


# list1 = [1,2,3,4,5,6]
# print(reverse_list(list1))



# reverse list items in the list          


# def reverse_element(l) :
#     element = []
#     for i in l:
#         element.append(i[::-1])
#     return element

# list1 = ['abc' , 'def' , 'xyz']
# print(reverse_element(list1))

# filter odd and even
def odd_even(l) :
    even = []
    odd = []
    total = []
    for i in l :
        if i%2==0 :
            even.append(i)
        else :
            odd.append(i)
    # total = [odd , even]
    total.append(odd)
    total.append(even)
    return total

list1 = [1,2,3,4,5,6,7,8,9]
print(odd_even(list1))