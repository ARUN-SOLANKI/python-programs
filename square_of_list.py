def list_square(l) :
    list2 = []
    for i in range(0,len(l)) :
            list2.append(l[i]**2)
    return list2

list1 = [1,2,3,4]
list3= [1,3,5,7]
list4 = [2,4,6,8]
list5 = [3,6,9,12]


print(list1)
print(list3)
print(list4)
print(list5)
print(list_square(list1))
print(list_square(list3))
print(list_square(list4))
print(list_square(list5))