"""Newton Rhapson Method for finding the real roots of many functions,
This however finds the real root of polynomial with one variable.
==========================================================================
                               Exercise 8
==========================================================================
Add code to this that keeps track of the number of iterations used to find
the root.  Use that code as part of a program that compares the efficiency of
Newton-Rapshon and bisection search.

"""
epsilon  = 0.01
k = 24.0
guess = k/2.0

while abs(guess* guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
print('Square root of', k, 'is about', guess)
