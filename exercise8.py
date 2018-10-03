"""Newton Rhapson Method for finding the real roots of many functions,
This however finds the real root of polynomial with one variable.
==========================================================================
                               Exercise 8
==========================================================================
Add code to this that keeps track of the number of iterations used to find
the root.  Use that code as part of a program that compares the efficiency of
Newton-Rapshon and bisection search.

"""
import exercise7

epsilon  = 0.01
k = 25.0
guess = k/2.0
interNumb = 0

while abs(guess* guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    print('Guess: ', guess, 'K', k)
    interNumb = interNumb + 1
print('Square root of', k, 'is about', guess)
print('Bisection search from ex7 requires: ', exercise7.numGuesses, 'iterations, while...')
print('Newton-Rhapson method requires: ', interNumb, 'iterations, ergo:')
if exercise7.numGuesses < interNumb:
    print('Bisection is more efficient')
else:
    print('Newton is more efficient')
