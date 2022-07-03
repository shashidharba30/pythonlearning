"""
function types
1.Built in functions
2.User-Defined functions
3.lambda function
"""

#built function like print(),input(),len(),sorted() and so on are function that come with python when installed
#check documentation of built in function help(function_name)
#user defined function these are the function that user created
#syntax
"""
def function_name(arguments [optional]):
    #statement - 1
    .
    .
    .
    #statement - n
"""

#function definition
#place where funtion is defined and its body
def sum_two():
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    c = a + b
    print(c)

print("function example")
sum_two()    # function is called and execution of funtion start from here

"""
TYPES OF ARGUMENTS IN FUNCTION
"""

def sum_two(a,b):
    c = a+b
    print(c)

#function with positional arguments
print("example of positional arguments")
a = int(input("enter first number"))
b = int(input("enter second number"))
sum_two(a,b)

#function with default arguments
def sum_two(a,b=0):
    c = a+b
    print(c)

print("function default arguments example")
a = int(input("enter first number"))
sum_two(a=a)

#function with keyword arguments
def sum_two(a,b):
    c = a+b
    print(c)

print("function keyword arguments")
sum_two(a=5,b=10)

#variable length arguments
# *args
# **kwargs
# starts are important not variable name

def sum_of_var(*item):
    print(item)
    print(type(item)) #type() fucntion used to check variable type
    return sum(item) # sum() function used to check sum of numbers

print("example of args example")
output = sum_of_var(5,6,7,8)
print(output)

def sum_of_var(**item):
    """
    @test
    program for keyword arguments
    ** means keyword arguments
    """
    print(item)
    print(type(item))
    return sum(item.values())

print("example  of kwargs example")
output = sum_of_var(a=5,b=6,c=7,d=8,e=9)
print(output)
print("function documentation example")
print(help(sum_of_var)) #check documentation of function
print(sum_of_var.__doc__)

# / for postion only arguments
# * for keyword only arguments

def sum_of_var(a,b,/,c,d):
    print(a+b+c+d)





