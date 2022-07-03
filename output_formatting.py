message = "A long ago far away ..."
print(message)

a = 10
b = 40.00
#print(message+str(a))

#output formatting
#first type
# %d - integer, %f - floating point, %s - string
message = "A long ago far away ... %d"%(a)
print(message)

#second type
message = "A long ago far away ... {0} {1}".format(a,b)
print(message)

#third type
message = f"A long ago far away ... {a} {b}"
print(message) 