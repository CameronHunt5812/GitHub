import math

print 'what is the number of sides of the polygon? Then the length of the sides?'
n = int(raw_input())
s = int(raw_input())

def cot(z):
    cot = 1/math.tan(z)
    return cot
    
cotPiN = cot(3.14159/n)
ar = (1/4.0)*n*(s**2)*cotPiN
print 'the area of the polygon is aprox: ' + str(ar)