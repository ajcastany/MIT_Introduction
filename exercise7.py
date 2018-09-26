"""
Finger Exercise 7:
=======================================================================
What would the code in figure 3.4 do if the statement x = 25 were replaced by x = -25
What would have to be changed to make the code work for finding an approximation
to the cube root of both negative and positive numbers?
(HINT: Think about changing low to ensure that the answer lies wityhin the region being searched)
"""

#Copy figure 3.4
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans**2 - abs(x)) >= epsilon: 							#bisection search, divides the search space in half at each step
	print('low = ', low, 'high = ', high, 'ans =', ans)
	numGuesses += 1
	if ans**2 < abs(x):
		low = ans
	else:
		high = ans
	ans = (high + low )/2.0

print('numGuesses = ', numGuesses)
