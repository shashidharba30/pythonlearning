"""
function types
1.Built in functions
2.User-Defined functions
3.lambda function
"""

"""
def a_name(x):
    return x+x
"""
x = int(input("enter a number"))
print((lambda x:x*2)(x))

add_one = lambda x:x+1
print(add_one(x))

# lambda function can also be used with built in functions like filter(), map(), reduce()
## filter ###

numbers = [-2, -1, 0, 1, 2]

# Using a lambda function
positive_numbers = filter(lambda n: n > 0, numbers)
positive_numbers

print(list(positive_numbers))


# Using a user-defined function
def is_positive(n):
    return n > 0

list(filter(is_positive, numbers))

## map ##
# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2, li))
print(final_list)

# Python code to illustrate
# reduce() with lambda()
# to get sum of a list

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)










