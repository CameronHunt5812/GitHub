#3x^2 + 2 = 2x + 3
#-2
#3x^2 = 2x+1
# /3
#x^2 = (2/3)x + 1
#


#x * m1 + c1 = x * m2 + c2
x = 0
print 'X * ?'
m1 = int(raw_input())
print 'x * ' + str(m1) + ' + ?'
c1 = int(raw_input())
print 'x * ' + str(m1) + ' + ' + str(c1) + ' = x * ?'
m2 = int(raw_input())
print 'x * ' + str(m1) + ' + ' + str(c1) + ' = x * ' + str(m2) + ' + ?'
c2 = int(raw_input())

c2 = c2 - c1
c1 = 0
m1 = m1 - m2
m2 = 0
c2 = c2 / m1
m1 = 1
x = c2
print '=============='
print 'x = ' + str(x)