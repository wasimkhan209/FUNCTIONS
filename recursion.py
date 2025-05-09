'''Recursion:-
             A programming technique where a function calls itself repeatedly 
Example:- '''

def show (n):
    if(n == 0):
        return 
    print(n)
    show (n-1)

show(5)
show(50)
show(10)