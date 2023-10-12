# check number is negative or positive
'''
x=int(input("input an integer : "))
if x>0:
    print("This is positive")
elif x<0: 
     print("This is negative")
else:
     print("Number is zero")
'''

# check number is even or not
'''
y=int(input("Enter a number : "))
if y%2==0:
    print("Number is even")
else:
     print("Number is odd")
'''

# and or operator
'''
x=5
y=8
z=1
if x>2 and y>2:
     print("x and y are greater than two")
if y%2==0 or z%2==0:
    print("One of y and z are even")
'''

#nested if

num=int(input("Enter the nnumber : "))
if num%15==0:
    print("Number is divisible by 15")
else:
    if num%3==0 or num%5==0:
        print("Number is not divisible by 15 but divisible by 3 or 5")
    else:
        print("Number is neither divisible by 15 nor with 3 or 5")