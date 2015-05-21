pi = 3.14159
r = 0
circle = 'circle'
rectangel = 'rectangle'
trapezoid = 'trapezoid'
print 'what shape do you have?'
choce = raw_input()

if choce == circle:
    print 'what is the radius?'
    temp = input()
    r = int(temp)
    aria = pi*(r**2)
    print 'the aria is, ' + str(aria)
elif choce == rectangel:
    print 'input the length of a side'
    s1 = raw_input()
    print 'input the length of a side'
    s2 = raw_input()
    aria = int(s1) * int(s2)
    print 'the aria is, ' + str(aria)
elif choce == trapezoid:
    print 'Input the length of a bace'
    b1 = raw_input()
    print 'Input the length of the other bace'
    b2 = raw_input()
    print 'Input the hight'
    h = raw_input()
    aria = ((int(b1) + int(b2))/2)*int(h)
    print 'the aria is, ' + str(aria)
elif choce == 'triangle':
    print 'input the bace'
    b1 = raw_input()
    print 'input the hight'
    h = raw_input()
    aria = (int(b1)*int(h))/2
    print 'the aria is, ' + str(aria)
#elif choce == :
#elif choce == :