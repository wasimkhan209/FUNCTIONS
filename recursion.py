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

# Factorial Recursion

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return factorial(n-1) * n
print(factorial(5)) # Ans = 120
print(factorial(4)) # Ans = 24
print(factorial(3)) # Ans =6
print(factorial(8)) # Ans = 40320 and so on ...

# write a prog that calculate the sum of first 10 natural number
def sum(n):
    if(n == 0 ):
        return 0
    return sum(n-1) + n
print(sum(10))

''' THE ANSWER WILL BE CALCULATED AS
Calculating sum(10):
Let's step through the recursive calls:

sum(1) = 0 + 1 = 1

sum(2) = 1 + 2 = 3

sum(3) = 3 + 3 = 6

sum(4) = 6 + 4 = 10

sum(5) = 10 + 5 = 15

sum(6) = 15 + 6 = 21

sum(7) = 21 + 7 = 28

sum(8) = 28 + 8 = 36

sum(9) = 36 + 9 = 45

sum(10) = 45 + 10 = 55
At the end Answer will be ("54") '''