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
    if(n == 0 or n == 1):
        return 0
    return sum(n-1) + n
print(sum(10))

''' THE ANSWER WILL BE CALCULATED AS
Calculating sum(10):
Let's step through the recursive calls:

sum(10) = sum(9) + 10

sum(9) = sum(8) + 9

sum(8) = sum(7) + 8

sum(7) = sum(6) + 7

sum(6) = sum(5) + 6

sum(5) = sum(4) + 5

sum(4) = sum(3) + 4

sum(3) = sum(2) + 3

sum(2) = sum(1) + 2

sum(1) = 0 (base case) 
At the end Answer will be ("54") '''