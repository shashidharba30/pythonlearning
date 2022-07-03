"""
CONTROL FLOW STATEMENTS
1.SEQUENTIAL STATEMENTS
2.SELECTION STATEMENTS
3.LOOPING/REPITATION STATEMENTS
"""

########==========LOOPING STATEMENTS===========================####################
## WHILE 
## FOR

i=0
while(i!=-1):
    print(i)
    i+=1
    if (i>9):
        i = -1

#for loop is used to loop through data structures like list,set,tuple,string,dictionary

a = ['a','b','c','d','e','f','g']
b = ""
for i in a:
    b = a+a
print(b)

#use of range function
# range(stop) if you pass only single arguments the it is stop arguments
#range(start,stop,[step]) range syntax
# range function takes three parameters start,stop,
# step start specifies where start and stop specifies where to stop and step is used how many digits to move from start
print("range with only stop argumnet")
for i in range(10):
    print(i)

print("range with start and stop")
for i in range(1,10):
    print(i)

print("range example")
for i in range(1,10,2):
    print(i)

#loop control keywords continue, pass, break
#pass acts like placeholder 
print("use of pass keyword")
for i in range(10):
    pass

print("use continue keyword")
for i in range(10):
    if i==3:
        continue
    else:
        print(i)

print("use of break keyword")
for i in range(10):
    if i>5:
        break 
    print(i)   









