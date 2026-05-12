'''
A recursion function (or recursive function) is a function that calls itself
'''

'''
factorial(n)= n * factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return  n * factorial(n-1)

n= int(input('enter a number'))
print(f"the factorial of this number is: {factorial(n)}")

'''
practice set
'''

'''
Find the greatest number using a function
'''
def greatest(a, b, c):
    if(a>b and a>c):
        return a 
    
    elif(b>a and b>c):
        return b
    
    else:
        return c 
    
a= 1
b= 4
c= 6
print(greatest(a, b, c))
 

def cm_to_inch(cm):
    return cm/2.54

cm = float(input("enter a inch in cm"))
print("inch", cm_to_inch(cm))


'''
prevent new line
'''

print('a')
print('b')
print('c', end='')
print('d', end=''),

'''
sum of first n natural numbers
'''

'''
sum(n) = sum(n-1) + n
'''

def sum(n):
    if(n==1):
        return 1
    return sum(n -1) + n
print(sum(3))