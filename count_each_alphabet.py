name = input(" enter your name ")
for i in range(0,len(name)) :
    print(f"{name[i]} :  {name.count(name[i])}")