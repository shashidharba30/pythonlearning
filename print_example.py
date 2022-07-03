"""
Syntax:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
print("hello","every")
\t = tab space
\\ = backslash
\b = backspace
\r = return
\n = newline
"""
#example
f = open("abc.txt","w")
print("hello","bhai",sep='\b',end='\t',file=f,flush=True)
f.close()

#Comments
#information to be displayed
#to add url link
#to stop execution of piece of code

#Comments three type 
#1.Single line comment - one line comment with #
#2.Multi line comment - multiple line comment with # # #
#3.DocString - ''' ''' / """ """

"""
My name is 
i am jskj

"""

print("end of comments")