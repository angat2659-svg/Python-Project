def avg():
    a = int(input("enter a number"))
    b = int(input("enter a number"))
    c = int(input("enter a number"))
    average = (a + b+ c)/3
    print(average)

avg()

'''
Greet
'''

def goodDay():
    print("good day")
goodDay()

'''
built in function len(), print(), range()
'''

'''
Function with argument
'''

def goodDay(name):
    print("good day", name)
goodDay("Angat")

'''
We can use multiple argument and params
'''
def goodDay(name, message):
    print("good day", name, message)
goodDay("Angat", "How are you")


'''
return value
'''

def goodDay(name, message):
    print("good day", name, message)
    return 'ok'
a = goodDay("Angat", "What are u doing")
print(a)

'''
Default parameter
'''

def goodDay(name, message = "tell me yor nearest future plan"):
    print("good day", name, message)
goodDay("Angat", "How are you")

'''
Another example is
'''

def goodDay(name, message = "tell me yor nearest future plan"):
    print("good day", name, message)
goodDay("Angat", )

def square(num , num1):
    print("are a that two number is", num * num1)
square(4,6)