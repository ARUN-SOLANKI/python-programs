#  common in the two list 

# def common(l1 , l2) : 
#     output = []
#     for i in l1:
#         if i in l2 :
#             output.append(i)
#     return output


# l1 = [1,2,8,9,5,4,2,1,5,4]
# l2 = [1,2,3,5,6,4]
# print(common(l1 , l2))



#  no of list inside list 

def count_list(l):
    count = 0
    for i in l :
        if type(i) == list :
            count += 1
    return count

list1 = [1,2,3,[1,2,3],[1,2,3],[1,2]]
print(count_list(list1)) 
