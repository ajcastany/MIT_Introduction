"""Newton Rhapson Method for finding the real roots of many functions,
This however finds the real root of polynomial with one variable.
==========================================================================
                               VARIABLES
==========================================================================
"""
epsilon  = 0.01
k = 24.0
guess = k/2.0

while abs(guess* guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
print('Square root of', k, 'is about', guess)
