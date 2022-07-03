"""
Opearators in Python
1.Arithmetic Operators
2.Comparison Operators
3.Logical Operators
4.Bitwise Operators
5.Assignment Operators
6.Identity Operators
7.Membership Operators
"""

"""
1.Arithmetic Operators
+ - add
- - subtract
* - multiply
/ - division(float)
// - division(floor)
% - Modulus - return remainder
** - first raise power to second
"""
print("Arithmetic opeator\n")
a = 10
b = 5
print(a+b)
print(b-a)
print(a*b)
print(b/a)
print(b//a)
print(b%a)
print(a**b)

"""
2.Comparison Operators
>
<
>=
<=
==
!=
"""
print("\nComparision operator\n")
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)


"""
3.Logical Operators
and
or
not
"""
print("\nLogical opearator\n")
print(a>0 and a != -1)
print(a>0 and a != -1)
print(not a)

"""
4.Bitwise Operators
& - and
| - or
~ - not
^ - xor
>> - right shift
<< - left shift
"""

print("\nBitwise Operator\n")
a = 10
b = 20
print(a&b)
print(a|b)
print(~a)
print(a^b)
print(a>>2)
print(a<<2)

"""
5.Assignment Operators

=	Assign value of right side of expression to left side operand 	x = y + z
+=	Add AND: Add right-side operand with left side operand and then assign to left operand	a+=b     a=a+b
-=	Subtract AND: Subtract right operand from left operand and then assign to left operand	a-=b     a=a-b
*=	Multiply AND: Multiply right operand with left operand and then assign to left operand	a*=b     a=a*b
/=	Divide AND: Divide left operand with right operand and then assign to left operand	a/=b     a=a/b
%=	Modulus AND: Takes modulus using left and right operands and assign the result to left operand	a%=b     a=a%b
//=	Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand	a//=b     a=a//b
**=	Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand	a**=b     a=a**b
&=	Performs Bitwise AND on operands and assign value to left operand	a&=b     a=a&b
|=	Performs Bitwise OR on operands and assign value to left operand	a|=b     a=a|b
^=	Performs Bitwise xOR on operands and assign value to left operand	a^=b     a=a^b
>>=	Performs Bitwise right shift on operands and assign value to left operand	a>>=b     a=a>>b
<<=	Performs Bitwise left shift on operands and assign value to left operand	a <<= b     a= a << b
"""

print("\n")
# Examples of Assignment Operators
a = 10

# Assign value
b = a
print(b)

# Add and assign value
b += a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# bitwise lishift operator
b <<= a
print(b)


"""
6.Identity Operators
is
is not
"""

a = 10
b = 20
c = a

print("\nIdentity Operators\n")
print(a is not b)
print(a is c)

"""
7.Membership Operators
is
is not
"""

print("\n Membership operator")
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
	print("x is NOT present in given list")
else:
	print("x is present in given list")

if (y in list):
	print("y is present in given list")
else:
	print("y is NOT present in given list")


