# list_demo = [i for i in range(1,11)]
# list_demo = [i for i in range(1,11) if i % 2 == 0 ]
# list_demo = [i if i % 2 == 0 else -i for i in range(1,11)]


# list_demo = [[1,2,3],[4,5,6],[7,8,9]
# list_demo = [[i for i in range(1,4)] for j in range(5)]


# excercise 1 
# def reverse_string(l) :
#     return [name[::-1] for name in l ]
# l = ['arun','solanki',"is","here"]
# print(reverse_string(l))


# excercise 2 
def reverse_string(l) :
    return [str(i)  for i in l if type(i) == int or type(i) == float ]



l = ['arun', 1,2,3,4.0,5.2,6.1,1,2,[1,2,3,],(1,2,3,),True,False]
print(reverse_string(l))

