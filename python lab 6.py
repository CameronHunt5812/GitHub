def add():
    print "How many numbers do you want to add?"
    loop = int(raw_input())
    num1 = 0
    for i in range(loop):
        print "enter a number"
        num1 = num1 + int(raw_input())
    print "the answer is " + str(num1)

def addList():
    list1 = []
    print "how many numbers do you want to add?"
    num1 = int(raw_input())
    for i in range(num1):
        print "enter a number"
        num2 = int(raw_input())
        list1.append(num2)
    print  str(sum(list1))

def factorial():
    