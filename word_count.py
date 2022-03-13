str = input("enter a string ")
print(str)
print(len(str))
string = str.strip()
last = ""
current = ""
main_string=""
for i in range(0,len(string)):
       if string[i]!=" ":
           main_string = main_string +  string[i]
           last=""
       else:
           if last == " ":
               current = ""
               last=" "
           else:
               current = " "
               main_string += current
               last = current
               
print("\n\n\n\n\n")    
print(main_string)
length = len(main_string)
print(f"length of the modify string is {length}")
space = main_string.count(" ")
word = space + 1;
character = length - space
print(f"total number of words is {word}")
print(f"total number of CHARACTER is {character}")
print(f"total number of space is {space}")
