"""
Finger Exercise 7:
=======================================================================
What would the code in figure 3.4 do if the statement x = 25 were replaced by x = -25
"""

#Copy figure 3.4
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon: 							#bisection search, divides the search space in half at each step
	print('low = ', low, 'high = ', high, 'ans =', ans)
	numGuesses += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high + low )/2.0

print('numGuesses = ', numGuesses)
