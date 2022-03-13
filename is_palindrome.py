def is_palindrome(string) :
    string2 = string[::-1]   
    return string2 == string 


string = input("enter a string \t")
print( is_palindrome(string) )

