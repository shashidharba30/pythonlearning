"""
CONTROL FLOW STATEMENTS
1.SEQUENTIAL STATEMENTS
2.SELECTION STATEMENTS
3.LOOPING/REPITATION STATEMENTS
"""

#EXAMPLE FOR SEQUENTIAL STATEMENTS
a = 10
b = 20
c = a + b
print("sequnetial statement example")
print(c)

#########==================SELECTION STATEMENT=============############
#IF STATEMENT
#IF ELSE STATEMENT
#IF ELIF STATEMENT
#IF ELIF ELSE STATEMENT
a = int(input("enter a number"))

if (a>0):
    print("natural number")

if (a>0):
    print("natural number")
else:
    print("unknow number {}".format(a))


if (a>0):
    print("natural number")
elif (a>=0):
    print("whole number")

if (a>0):
    print("natural number")
elif (a>=0):
    print("whole number")
else:
    print("unknow number {}".format(a))

# we can also neste the statements

if (a>=0):
    if(a>0):
        print("natural number")
    else:
        print("whole number")
else:
    if(a<0):
        print("integer number")                        
