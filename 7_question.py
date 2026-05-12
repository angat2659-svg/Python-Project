'''
greatest of given number
'''
a= int(input("enter a number 1:"))
b= int(input("enter a number 2:"))
c= int(input("enter a number 3:"))
d= int(input("enter a number :"))

if (a>b and a>c and a>d):
    print("greatest is a",a)

elif (b>a and b>c and b>d):
    print("greatest is b",b)

elif (c>b and c>a and c>d):
    print("greatest is c",c)

elif (d>b and d>c and d>a):
    print("greatest is d",d)


'''
to find whether a given username contains less than 10 or not?
'''
username = input("enter a user Name")
if(len(username)<10):
    print("your username contain less than 10 character")

else:
    print('your username contain more than or equal to 10 character')