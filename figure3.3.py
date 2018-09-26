"""
Exercise in Figure 3.3:
========================================================================
implements an algorith that finds an approximation to a square root.
"""

x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
	ans += step
	numGuesses += 1
print('NumGuesses = ', numGuesses)
if abs(ans**2 - x) >= epsilon:
	print('Failed on square root of,', x)
else:
	print(ans, 'is close to square root of', x)