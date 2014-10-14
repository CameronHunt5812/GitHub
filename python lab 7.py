# 25pts
num1 = 1
while (num1 < 300):
    print num1
    num1 = num1 + 2

#50pts
list1 = [20,48,5,29]
num2 = 0
while (num2 < len(list1)):
    print list1[num2]
    num2 = num2 + 1

#100pts
import random
rand = random.randint(0,50)
gess = int(raw_input())
while (rand != gess):
    if gess < rand:
        print "too low"
        gess = int(raw_input())
    else:
        print "too high"
        gess = int(raw_input())
print "you win"
