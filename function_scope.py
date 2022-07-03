#scope of a variable 
# there are two scope in program
#global or local or nonlocal
"""
A scope is a textual region of a Python program where a namespace is directly accessible. 
“Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

Although scopes are determined statically, they are used dynamically. At any time during execution, 
there are 3 or 4 nested scopes whose namespaces are directly accessible:

1.the innermost scope, which is searched first, contains the local names
2.the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
3.the next-to-last scope contains the current module’s global names
4.the outermost scope (searched last) is the namespace containing built-in names
"""

def func():
    print(s)

print("gloabla scope example")
s = "I love walking" #global scope
func()    
#function execution start from where you ar calling the function
#any variable outside the function if it is declared before calling the function the that variable global scope
#global scope means any function can access that variable
#https://docs.python.org/3/tutorial/classes.html
#https://docs.python.org/3/contents.html

def func():
    print("local scope example")
    s = "I love walking" #local scope
    print(s)

func()

##global scope cannot be changed without calling them global scope
#def func():
#     print("local scope example")
#     print(s)  
#     s = "I love walking" #local scope
#     print(s)
# func()
#UnboundLocalError: local variable 's' referenced before assignment

print("global scope example")
def func():
    global s
    print(s)
    s = "I love walking"
    print(s)
s = "I love eating"
func()
print(s)


##example of all three scope
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


