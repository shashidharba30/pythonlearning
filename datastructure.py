"""
DataStructures in Python
1.Arrays
2.Lists  --Built in datatype
3.Set     --Built in datatype
4.Tuple   --Built in datatype
5.Dictionary   --Built in datatype
6.Files
"""

# lists
a = [] #empty list
a = list() #empty list
a = ['a'] + ['b'] #list concatination
b = ['a','b','c','d','e','f','g','h','i']
#Lst[ Initial : End : IndexJump ] syntax of slicing
#inexjump means how many index to jump
#examples
print("below trying to display list slicing")
print(b[1:])
print(b[:5])
print(b[1:3])
print(b[::2])
print(b[-1])
print(b[::-1])
#built in methods in list
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
c = []
print(c) # empty list
print("Below list function use is displayed")
c.append(4)
print("after append")
print(c)
c.append(5)
print("after append")
print(c)
c.clear()
print("after clear")
print(c)
d = c.copy()
print("after copy")
print(d)
print("count of a character "+str(b.count('a')))
print("use of index function "+str(b.index('d')))
c.extend(b)
print("after extend function")
print(c)
c.insert(1,'z')
print("after insert function")
print(c)
c.remove('a')
print("after remove function")
print(c)
c.pop()
print("after pop function")
print(c)
c.sort()
print(c)

#set
a = {} #empty set
a = set()
# built in methods of set 
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

engineers = set(['John', 'Jane', 'Jack', 'Janice'])
print(engineers)
programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])
print(programmers)
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])
print(managers)
print("below set function is in use")
employees = engineers | programmers | managers # union
# you can also use union method for same
print(employees)           
engineering_management = engineers & managers            # intersection
print(engineering_management)
fulltime_management = managers - engineers - programmers # difference
print(fulltime_management)
engineers.add('Marvin')                                  # add element
print(engineers) 
set(['Jane', 'Marvin', 'Janice', 'John', 'Jack'])
print(employees.issuperset(engineers))     # superset test
employees.update(engineers)         # update from another set
print(employees.issuperset(engineers))
True
for group in [engineers, programmers, managers, employees]: 
     group.discard('Susan')          # unconditionally remove element
     print(group)

#Tuple
#  Built in method of tuple
#  'count', 'index'

#Tuple cration
t = tuple()
t = ()
# above both method create an empty tuple
t = (1,2,3,4,5)
print(t)
t = tuple([1,2,3,4,5])
print(t)

# you can access tuple by index
print(t[1])
# you cannot modify a tuple like below
#t[2] = 4

print("built in method use")
print(t.count(1)) #count the number of time a value is present in a tuple
print(t.index(2)) # print the index of first occurence of a value in a tuple

# Dictionay
# built in methods
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
a = {}
a = dict()
print(a)
# above methods create a empty dictionary
# dictionary contains only key value pairs

#ways of creating a dictionary
a = {'a':1,'b':2,'c':'abc','d':True}
print(a)
key = ['a','b','c','d']
values = [1,2,'abc',True]
a = dict(zip(key,values))
print(a)
b = dict()
b['a'] = 1
b['b'] = 2
b['c'] = 'abc'
b['d'] = True
print(b)

#built in function in use
print("use of clear method")
print(a.clear())
print("use of copy method")
c = b.copy()
print("use of copy")
print(c)
d = b.get('a')
print("use of get method")
print(d)
print("use of items method")
print(b.items())
print("use of keys method")
print(b.keys())
print("use of values")
print(b.values())
print("use of pop")
print(b.pop('a'))
print("use of pop items")
print(b.popitem())
print(b)
b.update(b=10)
print("use of update")
print(b)
b.setdefault('default','None')
print("use of set default")
print(b)
key1= ('k1','k2','k3')
value = 0
newdict = dict.fromkeys(key1,value)
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print("use of fromkeys")
print(newdict)
print(thisdict)




