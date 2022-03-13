def fibonacci_series(n) :
    first_number = 0
    second_number = 1
    if n==1 :
        print(first_number)
    elif n==2 :
        print(first_number,second_number)
    else :
        print(first_number,second_number, end = " ")
        for i in range(n-2) :
            next_number = first_number + second_number
            first_number = second_number
            second_number =next_number
            print(second_number , end=" ") 




n = int(input("enter a number"))
fibonacci_series(n)