'''Recursion:-
             A programming technique where a function calls itself repeatedly 
Example:- '''

# def show (n):
#     if(n == 0):
#         return 
#     print(n)
#     show (n-1)

# show(5)
# show(50)
# show(10)

# Factorial Recursion

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return factorial(n-1) * n
print(factorial(5)) # Ans = 120
print(factorial(4)) # Ans = 24
print(factorial(3)) # Ans =6
print(factorial(8))