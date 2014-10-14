print "How many numbers do you want to add?"
loop = int(raw_input())
num1 = 0
for i in range(loop):
    print "enter a number"
    num1 = num1 + int(raw_input())
print "the answer is " + str(num1)