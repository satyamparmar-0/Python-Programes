# a==b is a conditional statement 
# a!=b is a not equal to 
# a<=b a is less than equal to b

a= int(input("enter any number "))
if a%2==0:
    print("number is even ")
else:
    print("number is odd")
b = int(input("enter any number "))
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")

# "and" keyword for multiplication if any condition is false than output is false
# "or" keyword for addition if any condition is true output is true

c = int(input("enter any number "))
if a>b and a>c:
    print("a is greater than all numbers ")
elif a<b or a<c:
    print("any one condition is true")

else:
    print("b or c is greater ")

# "pass" keyword is used for do nothing and avoid the error while executing the code

if a>b:
    print("a is greater than b")
    pass

# here calculating pass and fail 
percentage=(a+b+c)/3
if percentage>33:
    print("student is pass")
else:
    print("student is fail")

spam = ["make money","suscribe this","click here","secured"]
words= input("enter to check spam words ")
if words in spam:
    print("that words is not secure")
else:
    print("you are secure")