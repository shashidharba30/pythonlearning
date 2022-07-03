# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

#__name__ set "__main__"  by adding this piece of code at end of your moduel
# you can make the file usable as script as well as an imported module
# because the code that parses the command line only runs if the module is executed as the “main” file
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    fib2(int(sys.argv[1]))
        