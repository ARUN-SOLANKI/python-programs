# more then one input in single line due split()
# diffrent methods to print statements using or without using .format() and f
# how to convert string into number-------------- int(string)
# how to convert number into string ------------- str(number)




number_1, number_2, number_3 = input("enter three numbers saprated by comma").split(",")
average = (int(number_1) + int(number_2) + int(number_3))/3;
# print("average of" + str(number_1) + "and" + str(number_2) + "and" + str(number_3) + "is" + str(average))
# print("average of {} and {} andn {} is {}".format(number_1 , number_2 , number_3 , average))
# print(f"average of {number_1} {number_2} and {number_3} is {average}")
# print("average of three numbers is {}".format(average))    
# print(f"average of three numbers is {average}")    
print("average of three numbers is " + str(average))