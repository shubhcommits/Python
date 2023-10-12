#string
name="Shubham"

print(type(name))  # this will print type of the variable

#integer
roll_no=58

#floating number
percentage = 94.2

#boolean
is_student=True

print(name,roll_no,percentage,is_student)

percentage=95.8  #updating varibale value of previous declared variable
print(percentage)

#concatination of variables
# different type variables can not be concatenated
# we use comma to print different dataType in same line
print("My name is "+name+" and my Roll no is ",roll_no)
print("I scored ",percentage," in my last exam I am a student ",is_student)
#printig Expression
print("My percentage is changed to ",percentage-1)
#printing with seperators
print(name,roll_no,percentage,is_student,sep="-")
x=1
y=2
z=3
print(x,y,z,sep="++++++++")  #By default space added in between them