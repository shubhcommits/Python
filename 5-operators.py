#Operator
# ** is Exponentiation  -> n**2  This is square of n
# // floor division  -> This return nearest whole number

# logical operator
exp1=5>6
exp2=5<6
print("exp1 and exp2",exp1 and exp2)
print("exp1 or exp2",exp1 or exp2)
print("Not exp1",not(exp1))

# identity operators
x=5
y=5
print("if x is y:",x is y) 
print("is x is not y",x is not y)

#membership operators
fruits=["apples","mango","banana"]
print("if mango is in fruits","mango" in fruits)
print("if cherry is not in fruits", "cherry" not in fruits)

#bitwise operator
a=5
b=3
print("a AND b",a&b)
print("a OR b",a|b)
print("a XOR b",a^b)

# operator precedence of python
# ()-**-//,/,%-*-+,-