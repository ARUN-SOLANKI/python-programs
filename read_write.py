f = open('abc.txt' ,  'w')
print(f.write("one is the best and now lorem100 \n haisuhf hahf shfauh jakh"))

f = open('abc.txt' ,  'r')
print(len(f.readline()))

for l in f:
    print(l)