"""
Finger Exercise #6 in MIT Introduction to Programing
=============================================================================================
Let s be a string that contains a sequence of decimal numbers separated by commas, e.g., s = '1.23,2.4,3.123'.  Write a program that prints the sum of the numbers in s.
"""
s = '1.23,2.4,3.123'
x = ''
y = 0.0
z = 0.0
for i in s:
    if i == ',':                # when for loop reaches end of string this doesn't get eval
        y = x
        x = ''
        z = float(y) + float(z)
        #print(y)
    else:
        x = x + i               # but x still has the value of the last string
z = z + float(x)                # So we add it here
print(z)                        # and print it here.
